import os
import glob
from log_command import log_command
from paths import GetPaths
import mapping
import helpers
from split_by_chr import split_bam_by_chr, get_bam_by_chr
import shutil


class PreProcessing(object):

    def __init__(self, working_directory, map_type, sample_type, library_matching_id, thrds, issplitchr):
        self.get_paths = GetPaths()
        self.main_directory = working_directory
        self.folder_directory = working_directory + "/" + map_type
        self.working_directory = working_directory + "/" + map_type + "/Mapping"
        self.map_type = map_type
        self.sample_type = sample_type
        self.library_matching_id = library_matching_id
        self.threads = thrds
        self.bundle_dir = self.get_paths.ref_dir + "hg19_bundle"
        self.split_chr = issplitchr
        self.file_list = []
        os.chdir(self.working_directory)

    def merge_bams(self, info_dict, all_bam_files):
        print("preprocess merge bams ")
        print(all_bam_files)
        inputs_list = ""

        for i in all_bam_files:
            inputs_list = inputs_list + "I=" + i + " "
        ouput_name = self.map_type + "_" + info_dict["Sample_ID"][0] + "_MergedBAM.bam"
        merge_command = "java -XX:ParallelGCThreads=" + self.threads + \
                        " -jar " + self.get_paths.picard_path + " MergeSamFiles " + inputs_list + \
                        " O=" + ouput_name + " USE_THREADING=true"

        log_command(merge_command, "Merge Bams", self.threads, "PreProcessing")
        return ouput_name

    def mark_duplicate(self, merged_bam, spark_option=False):
        if spark_option:
            mark_prefix_removed = "MDUP"
            output = mark_prefix_removed + "_" + merged_bam
            marked_dup_metrics = "marked_dup_metrics.txt"
            gatksparkdcommand = self.get_paths.gatk4_path + " MarkDuplicatesSpark -I " + merged_bam + \
                            " -O " + output + " -M " + marked_dup_metrics + " --remove-all-duplicates TRUE  --create-output-bam-index TRUE "
            log_command(gatksparkdcommand, "Mark Duplicate Spark", self.threads, "PreProcessing")
            self.file_list.append(marked_dup_metrics)
            self.file_list.append(output+".bai")
            self.file_list.append(output + ".sbi")
            return output

        else:
            mark_prefix_removed = "MDUP"
            output = mark_prefix_removed + "_" + merged_bam

            picardcommand = "java -XX:ParallelGCThreads=" + self.threads + \
                            " -jar " + self.get_paths.picard_path + " MarkDuplicates I=" + merged_bam + \
                            " O=" + output + " M=marked_dup_metrics.txt REMOVE_DUPLICATES=true CREATE_INDEX=true"
            log_command(picardcommand, "Mark Duplicate", self.threads, "PreProcessing")
            self.file_list.append("marked_dup_metrics.txt")
            return output

    def pre_process(self, info_dict, all_bam_files):
        merged_file = self.merge_bams(info_dict, all_bam_files)
        indexed = helpers.create_index(merged_file, "Create Index by Merge", self.threads, "Pre Processing")
        self.file_list.append(merged_file)
        self.file_list.append(indexed)
        mark_duplicate_file = self.mark_duplicate(merged_file, True)
        print("preprocess mark duplicate file " )
        print(mark_duplicate_file)
        self.file_list.append(mark_duplicate_file)
        indexed = helpers.create_index(mark_duplicate_file, "Create Index by MarkDuplicate", self.threads,
                             "Pre Processing")
        self.file_list.append(indexed)
        helpers.create_folder(self.working_directory, self.file_list, map_type=self.map_type, step="PreProcess",
                              folder_directory=self.folder_directory)
        return mark_duplicate_file


# if __name__ == "__main__":
#     pre_processing_step = PreProcessing(working_directory="/home/bioinformaticslab/Desktop/testData",
#                            map_type="Bwa", sample_type="Tumor", library_matching_id="203", thrds="1", issplitchr="No")
#
#     mapping_step = mapping.Mapping(working_directory=pre_processing_step.main_directory,
#         map_type="Bwa", sample_type="Tumor", library_matching_id="203", thrds="3", trim="No")
#
#     fastq_list = helpers.get_fastq()
#     info_dict = helpers.get_info("Tumor", fastq_list)
#     os.chdir(pre_processing_step.working_directory)
#     bam_files = glob.glob("SortedBAM*.bam")
#     mark_duplicate_file = pre_processing_step.pre_process(info_dict, bam_files)
#     print(mark_duplicate_file)