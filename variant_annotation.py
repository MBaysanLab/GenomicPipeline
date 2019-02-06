import os
import glob
from log_command import log_command
from paths import GetPaths
import helpers
import pandas as pd
import shutil


class VariantAnnotation(object):

    def __init__(self, variant_annotater, wd, sample_name, thread_v, will_annotate, annotate_all):
        self.get_paths = GetPaths()
        self.working_directory = wd
        os.chdir(self.working_directory)
        print(self.working_directory)
        self.sample_name = sample_name
        self.v_annotater = variant_annotater
        self.threads = str(thread_v)
        if annotate_all:
            self.annotate_files = glob.glob("*.vcf")
        else:
            self.annotate_files = will_annotate
        self.humandb = self.get_paths.annovar + "humandb_38/"
        self.xref = self.get_paths.annovar + "example/gene_fullxref.txt"
        self.annovar_dir = self.get_paths.annovar + "table_annovar.pl"
        self.file_list = []

    def run_annotation(self):
        if self.v_annotater == "Annovar":
            self.annovar_vcf_files(self.annotate_files)

    def annovar_vcf_files(self, input_fs):
        print(input_fs)
        if type(input_fs) == list:
            for input_f in input_fs:
                input_file = self.working_directory + "/" + input_f
                output_f = "Annovar_" + "_".join(input_f.split(".")[:-1])
                output_file = self.working_directory + "/" + output_f
                command = self.annovar_dir + " --vcfinput " + input_file + " " + self.humandb + \
                          " -buildver hg38 -out " + output_file + " -remove -protocol refGene,ensGene,knownGene," \
                                                                 "cytoBand" \
                                                                  ",exac03,avsnp150,dbnsfp35c,gme,gnomad_exome," \
                                                                  "clinvar_20180603,cosmic -operation " \
                                                                  "gx,gx,gx,r,f,f,f,f,f,f,f -nastring . -polish " \
                                                                  "-xreffile " + self.xref
                print(command)
                log_command(command, "Annovar", self.threads, "Variant Annotation")
                output_fs = glob.glob("*" + output_f + "*")
                self.file_list.extend(output_fs)
            helpers.create_folder(self.working_directory, self.file_list, step="Annovar",
                                  folder_directory=self.working_directory)
        else:
            return False

def annovar_custom_txt(txt_file, vcf_file):
    data = []
    with open(txt_file) as f:
        columns_ = f.readline()
        cols = columns_.split("\t")
        print(cols)
        for line in f:
            data.append(line.split("\t"))
    df = pd.DataFrame(data)
    cols.append("ess")
    cols.append("ReadCount")
    headers = []
    with open(vcf_file) as f:
        for line in f:
            if line[:2] == "##":
                print(line)
            elif line[:6] == "#CHROM":
                headers.extend(line.split("\t"))
                print(headers)

    cols.extend(headers)
    df.columns = cols
    df.head()
    output_file_name = "Merged_" + txt_file.split("/")[-1]
    df.to_csv(output_file_name)


if __name__ == "__main__":
    annotate = VariantAnnotation(variant_annotater="Annovar", thread_v=4,
                            wd="/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/txts/40",
                            sample_name="S40", will_annotate=["INDEL_Varscan_Bwa_40_Cov8.vcf"], annotate_all=True)

    annotate.run_annotation()
