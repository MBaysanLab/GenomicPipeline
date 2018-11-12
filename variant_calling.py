import os
import glob
from log_command import log_command
from paths import GetPaths
import shutil
import subprocess
import tempfile


class VariantCall(object):

    def __init__(self, variant_caller, thrds, map_type, germline_bam, wd, tumor_bam, sample_name, tumor_only,
                 tumor_interval=None, germline_interval=None):
        self.get_paths = GetPaths()
        self.working_directory = wd
        # self.folder_directory = wd + "/" + map_type
        # self.working_directory = wd + "/" + map_type + "/GatkPreProcess"
        os.chdir(self.working_directory)
        print(self.working_directory)
        self.v_caller = variant_caller
        self.output_name = self.v_caller + "_" + sample_name
        self.threads = str(thrds)
        self.map_type = map_type
        self.ref_dir = self.get_paths.ref_dir + "hg19_bundle/ucsc.hg19.fasta"
        self.tumor_bam = tumor_bam
        self.germline_bam = germline_bam
        if tumor_only == "Yes":
            self.tumor_only_mode = True
        else:
            self.tumor_only_mode = False
        if variant_caller == "Mutect2_gatk3":
            self.tumor_interval = tumor_interval
            self.germline_interval = germline_interval
            self.realign_target = self.tumor_interval + " " + self.germline_interval

    def run_pipeline(self):
        if self.tumor_only_mode:
            if self.v_caller == "Mutect2":
                self.mutect_tumor_only()
                files = glob.glob("*.vcf*")
                self.create_folder(files)
        else:
            if self.v_caller == "Mutect2":
                self.mutect_caller()
                files = glob.glob("*.vcf*")
                self.create_folder(files)
            elif self.v_caller == "Varscan":
                self.varscan_caller()
                files = glob.glob("*.vcf*")
                self.create_folder(files)
            elif self.v_caller == "Mutect2_gatk3":
                self.mutect_caller_gatk3()
                files = glob.glob("*.vcf*")
                self.create_folder(files)
            elif self.v_caller == "Strelka":
                self.strelka_caller()
            else:
                return False
        return False

    def mutect_caller_gatk3(self):
        mutect_output = self.working_directory + "/" + self.output_name
        nct = " -nct " + self.threads
        command = "java -jar " + self.get_paths.gatk_path + " -T MuTect2 " + nct + " -R " + self.ref_dir + \
                  " -I:tumor " + self.tumor_bam + " -I:normal " + self.germline_bam + \
                  " -o " + mutect_output
        print(command)
        log_command(command, "Mutect2", self.threads, "Variant Calling")

    def mutect_caller(self):

        mutect_output = self.working_directory + "/" + self.output_name + ".vcf"
        normal_s_name = self.get_sample_name(self.germline_bam)
        tumor_s_name = self.get_sample_name(self.tumor_bam)

        #if normal_s_name==
        command = self.get_paths.gatk4_path + " Mutect2 " + " -R " + self.ref_dir + " -I " + self.tumor_bam + " -tumor "\
                  + tumor_s_name + " -I " + self.germline_bam + " -normal " + normal_s_name + " -O " + mutect_output
        print(command)
        log_command(command, "Mutect2", self.threads, "Variant Calling")
        self.mutect_select_variant(mutect_output)

    def mutect_tumor_only(self):
        mutect_output = self.working_directory + "/" + "TumorOnly_" + self.output_name + ".vcf"
        tumor_s_name = self.get_sample_name(self.tumor_bam)
        command = self.get_paths.gatk4_path + " Mutect2 -R " + self.ref_dir + " -I " + self.tumor_bam + " -tumor " + \
                  tumor_s_name + " -O " + mutect_output
        print(command)
        log_command(command, "Mutect2", self.threads, "Variant Calling Tumor Only")
        self.mutect_select_variant(mutect_output)

    def mutect_select_variant(self, mutect_output):
        self.mutect_select_variant_snp(mutect_output)
        self.mutect_select_variant_indel(mutect_output)
        self.mutect_select_variant_other(mutect_output)

    def mutect_select_variant_snp(self, mutect_output):
        snp_output = "SNP_" + mutect_output
        command = self.get_paths.gatk4_path + " SelectVariants -R " + self.ref_dir + " -V " + mutect_output + \
                  " --select-type-to-include SNP -O " + snp_output
        print(command)
        log_command(command, "Mutect2", self.threads, "Select SNP Variants")
        print(snp_output)

    def mutect_select_variant_indel(self, mutect_output):
        indel_output = "INDEL_" + mutect_output
        command = self.get_paths.gatk4_path + " SelectVariants -R " + self.ref_dir + " -V " + mutect_output + \
                  " --select-type-to-include INDEL -O " + indel_output
        print(command)
        log_command(command, "Mutect2", self.threads, "Select INDEL Variants")
        print(indel_output)

    def mutect_select_variant_other(self, mutect_output):
        indel_output = "OTHER_" + mutect_output
        command = self.get_paths.gatk4_path + " SelectVariants -R " + self.ref_dir + " -V " + mutect_output + \
                  " --select-type-to-exclude INDEL --select-type-to-exclude SNP -O " + indel_output
        print(command)
        log_command(command, "Mutect2", self.threads, "Select OTHER Variants")
        print(indel_output)

    def varscan_caller_step1(self):

        snp_output = self.working_directory + "/SNP_" + self.output_name
        indel_output = self.working_directory + "/INDEL_" + self.output_name
        command = "samtools mpileup -f " + self.ref_dir + " -q 1 -B " + self.germline_bam + " " + \
                  self.tumor_bam + " | java -jar " + self.get_paths.varscan_path + " somatic --output-snp " \
                  + snp_output + " --output-indel " + indel_output + \
                  " --mpileup 1 --min-coverage 8 --min-coverage-normal 8 --min-coverage-tumor 6 --min-var-freq 0.10 " \
                  "--min-freq-for-hom 0.75 --normal-purity 1.0 --tumor-purity 1.00 --p-value 0.99 " \
                  "--somatic-p-value 0.05 " + "--strand-filter 0 --output-vcf"
        print(command)
        log_command(command, "Varscan Step Pileup", self.threads, "Variant Calling")
        intermediate_varscan_somatic = glob.glob("*" + self.output_name + "*vcf*")

        return intermediate_varscan_somatic

    def varscan_caller_step2(self, intermediate_varscan_somatic):
        print(intermediate_varscan_somatic)
        for somatic in intermediate_varscan_somatic:
            command = "java -jar " + self.get_paths.varscan_path + " processSomatic " + somatic + \
                      " --min-tumor-freq 0.10 --max-normal-freq 0.05 --p-value 0.07"
            log_command(command, "Varscan Step Process Somatic", self.threads, "Variant Calling")
        return glob.glob("*vcf*")

    def varscan_caller(self):
        step1 = self.varscan_caller_step1()
        step2 = self.varscan_caller_step2(step1)
        print(step2)

    def strelka_caller(self):
        command = self.get_paths.strelka + " --normalBam " + self.germline_bam + " --tumorBam " + self.tumor_bam + \
                  " --referenceFasta " + self.ref_dir + " --runDir " + self.working_directory
        log_command(command, "Strelka Create Workflow", self.threads, "Variant Calling")
        run_workflow_command = "python runWorkflow.py -m local -j " + self.threads
        log_command(run_workflow_command, "Strelka Create Workflow", self.threads, "Variant Calling")

    def create_folder(self, all_files):
        up_dir = str(self.working_directory).split("/")[:-1]
        mk_dir = "/".join(up_dir) + "/" + self.v_caller
        print("**************MKDIR 1 ***************")
        os.mkdir(mk_dir)
        print(mk_dir)
        print("**************MKDIR 2 ***************")
        for file in all_files:
            if file[-2:] != "gz":
                print(file)
                shutil.move(self.working_directory + "/" + file, mk_dir + "/" + file)

    def get_sample_name(self, bamfile):
        command = "samtools view -H " + bamfile
        cmd = command.split(" ")
        try:
            with tempfile.TemporaryFile() as tempf:
                proc = subprocess.Popen(cmd, stdout=tempf)
                proc.wait()
                tempf.seek(0)
                output_split = str(tempf.read()).split("\\n")
                for a in output_split:
                    rg = a[:3]
                    if rg == "@RG":
                        get_sm = a.split("\\t")
                        for sm in get_sm:
                            if sm[:2] == "SM":
                                print(sm[3:])
                                return sm[3:]
        except:
            return False

#variant_caller, thrds, map_type, germline_bam, germline_interval, wd, tumor_bam, tumor_interval
if __name__ == "__main__":
    mutectvcf = VariantCall(variant_caller="Strelka", thrds=1, map_type="Bwa",
                            germline_bam="/home/bioinformaticslab/Desktop/AMBRY/DUYGU_1/Sample_40/Bwa/PreProcess/GATK_PRIR_MDUP_Bwa_40_MergedBAM.bam",
                            wd="/home/bioinformaticslab/Desktop/AMBRY/DUYGU_1/Sample_41/Bwa/PreProcess",
                            tumor_bam="GATK_PRIR_MDUP_Bwa_41_MergedBAM.bam",
                            tumor_interval="MDUP_Bwa_41_MergedBAM_realign_target.intervals", sample_name="41",
                            tumor_only="No")
    mutectvcf.run_pipeline()
