import os
from log_command import log_command
from paths import GetPaths
import helpers
import glob
import re
import gzip



class Mapping(object):

    """
    This class basically contain 1 main function and 2  complementary function and 2 helper function.
    Main purpose of this class is aligning raw fastq file data according to reference genome and
    create mapped bam file.

    This file will be in process in sorting and indexing functions and return Sorted and Indexed files
    with .bam and .bai extensions.

    There is also 2 helper functions in order to get files and information for files.

    Key function is mapping function. This function create a script in string format and give it to linux system and
    run algorithms in terminal


    Attributes
    ----------
    working_directory : str
        file path which contains .fastq.gz files.
    map_type : str
        option for mapping algorithm, BWA or Bowtie2
    sample_type : str
        type of sample, Tumor or Germline(Normal)
    library_matching_id : str
        id of patient who has got sample
    thrds : int
        number of core that wanted to use

    Methods
    -------
    get_fastq():
        Get fastq files inside working directory and return it as list
    get_info(fastq_list):
        Get information from sample file and return a information form in dictionary
    mapping():
        Map fastq files according to reference genome and return bam files. Bwa and Bowtie2 are options.
    convert_sort():
        Sort bam files
    create_index():
        Create index for bam files
    create_folder():
        Move files which created in this step to Mapping folder
    """

    def __init__(self, working_directory, map_type, sample_type, library_matching_id, thrds, trim):
        """
        Parameters
        ----------
        working_directory : str
            The folder directory of where fastq files are in
        map_type : str
            Mapping algorithm decision: Bwa or Bowtie2
        sample_type : str
            Type of sample: Tumor or Germline
        library_matching_id : str
            ID of patient which own the sample
        thrds : str
            Number of cores that wanted to use
        bundle_dir : str
            Path directory for reference files
        file_list : str
            List of files that created in this step
        """
        self.get_paths = GetPaths()
        if working_directory[-1] == "/" or working_directory[-1] == "\\":
            self.working_directory = working_directory[:-1]
        else:
            self.working_directory = working_directory
        self.map_type = map_type
        self.sample_type = sample_type
        self.library_matching_id = library_matching_id
        self.threads = str(thrds)
        self.bundle_dir = self.get_paths.ref_dir + "hg19_bundle"
        self.trim = trim
        self.file_list = []
        os.chdir(self.working_directory)

    def mapping(self):

        """
        End of this function mapping job is done in terms of selected mapping algorithms Bwa or Bowtie2. There is 5
        important step in this function.
        - First is reading a fastq file first line in order to get information given
        by sequence machine.
        - Second thing is creating table by same group of paired-end reads and lanes for mapping.
        - Thirdly, adding a custom read group information and give it to mapping alghorithm. This information will be
        in bam files which are created in this step.
        - Fourthly, creating a complete script as string type.
        - Lastly, created script is given to linux terminal system. The point is algorithms must be in path


        """
        fastq_list = helpers.get_fastq(self.trim)
        info_dict = helpers.get_info(self.sample_type, fastq_list)
        RG_SM = info_dict["Sample_ID"][0]
        RG_PL = "Illumina"
        RG_LB = self.library_matching_id
        first_fastq_file_dir = self.working_directory + "/" + fastq_list[0] + ".fastq.gz"
        with gzip.open(first_fastq_file_dir) as f:
            first_line = f.readline()

        flowcell_info = str(first_line).split(":")[2]

        for i in info_dict["Lanes"]:
            for k in info_dict["Number_of_seq"]:
                r1 = re.compile(".*" + i + "_R1_" + k)
                read1 = [s + ".fastq.gz" for s in fastq_list if r1.match(s)]

                r2 = re.compile(".*" + i + "_R2_" + k)
                read2 = [s + ".fastq.gz" for s in fastq_list if r2.match(s)]

                RG_ID = flowcell_info + "." + i[-1]
                RG_PU = flowcell_info + "." + info_dict["Index"][0] + "." + i[-1]
                map_bam = ""
                gene_origin = self.map_type + "_" + info_dict["Sample_ID"][0] + "_" + info_dict["Index"][
                    0] + "_" + i + "_" + k + ".bam"

                if self.map_type == "Bwa":
                    add_read_group = ' -R "@RG\\tID:' + RG_ID + '\\tSM:' + RG_SM + '\\tLB:' + RG_LB + '\\tPL:' + \
                                     RG_PL + '\\tPU:' + RG_PU + '" '

                    map_bam = "bwa mem -t " + self.threads + " " + add_read_group + self.get_paths.ref_dir + \
                              "Bwa/ucsc.hg19.fasta " + read1[0] + " " + read2[0] + \
                              " | samtools view -@" + self.threads + " -bS - > " + gene_origin
                    print("mapping" + map_bam)
                elif self.map_type == "Bowtie2":

                    add_read_group = " --rg-id " + RG_ID + " --rg SM:" + RG_SM + " --rg LB:" + RG_LB + " --rg PL:" + \
                                     RG_PL + " --rg PU:" + RG_PU

                    map_bam = "bowtie2 -p" + self.threads + add_read_group + " -x " + self.get_paths.ref_dir + \
                              "Bowtie2/hg_19_bowtie2 -1 " + read1[0] + " -2 " + read2[0] + \
                              " | samtools view -@" + self.threads + " -bS - > " + gene_origin
                else:
                    return "Please specify the map type Bwa/Bowtie "

                log_command(map_bam, "Mapping", self.threads, "Mapping")
                self.file_list.append(gene_origin)
                self.convert_sort(gene_origin)

        all_sortedbam_files = glob.glob("SortedBAM*.bam")
        helpers.create_folder(self.working_directory, self.file_list, map_type=self.map_type, step="Mapping")
        print("print sorted all bam files ")
        print(all_sortedbam_files)
        return all_sortedbam_files

    def convert_sort(self, sort_gene_origin):
        convert_sort = "samtools view -@" + self.threads + " -bS " + sort_gene_origin + " | samtools sort -@" + \
                       self.threads + " -o SortedBAM_" + sort_gene_origin
        log_command(convert_sort, "Convert Sort", self.threads, "Mapping")
        self.file_list.append("SortedBAM_" + sort_gene_origin)
        helpers.create_index("SortedBAM_" + sort_gene_origin, "Create Index", self.threads, "Mapping")







if __name__ == "__main__":
    mapping_step = Mapping(working_directory="/home/bioinformaticslab/Desktop/AMBRY/DUYGU_1/Sample_37",
                           map_type="Bwa", sample_type="Tumor", library_matching_id="11111", thrds="6")
    mapping_files = mapping_step.mapping()
    print(mapping_files)