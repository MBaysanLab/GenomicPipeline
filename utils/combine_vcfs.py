import os, fnmatch, glob
import pandas as pd
from utils.log_command import log_command
from paths import GetPaths
import variant_annotation
import re


class prel_analysis():

    def __init__(self, folder):
        self.folder = folder
        self.get_paths = GetPaths()
        self.ref_dir = self.get_paths.ref_dir + "Homo_sapiens_assembly38.fasta"

    def get_combine_all(self):
        initial = os.getcwd()
        os.chdir(self.folder)
        all_txt_m = glob.glob("Annovar*.txt")
        s_or_i = all_txt_m[0].split("_")[1]
        samples = self.mut_var(all_txt_m)
        print(samples)
        for sample in samples:
            sample_list_txt = glob.glob("Annovar_" + s_or_i + "*" + sample + "*.txt")
            sample_list_txt.sort()
            sample_list_vcf = glob.glob("Annovar_" + s_or_i + "*" + sample + "*.vcf")
            sample_list_vcf.sort()
            zipped = self.zipper(sample_list_txt, sample_list_vcf)

            df_lists = self.annovar_custom_txt(zipped)

            # print(df_lists)

            common = []
            common_df = self.sacma(df_lists, common)[0]
            common_df.to_csv(sample + "_commons_df_" + s_or_i.lower() + ".txt", sep="\t", index=False)
        os.chdir(initial)

    def mut_var(self, file_list):
        list_of_samples = set()
        for files in file_list:
            list_of_samples.add(files.split("_")[4].split(".")[0])
        return list_of_samples

    def annovar_custom_txt(self, zipped_file):
        df_list = []
        for txt_file, vcf_file in zipped_file:
            data = []
            with open(txt_file) as f:
                columns_ = f.readline()
                columns_ = columns_.replace("\n", "")
                cols = columns_.split("\t")
                for line in f:
                    data.append(line.replace("\n", "").split("\t"))
            df = pd.DataFrame(data)
            cols.append("zero")
            cols.append("ReadCount")
            headers = []
            with open(vcf_file, encoding="latin-1") as f:
                for line in f:
                    if line[:6] == "#CHROM":
                        headers.extend(list(
                            map(lambda x: x + "_vcf_" + "_".join("_".join(txt_file.split("_")[1:5]).split(".")[:2]),
                                line.replace("\n", "").split("\t"))))

            cols.extend(headers)
            df.columns = cols
            df.insert(loc=3, column="merged", value=df["Chr"] + "-" + df["Start"] + "-" + df["End"])
            df_list.append(df)
        return df_list

    def concat_list(self, df1, df2):
        ortak, last_two = list(df1.columns)[:-13], list(df1.columns)[-2:]
        df_den = pd.merge(df1, df2, how="inner", on=ortak)
        len_ortak = len(ortak)
        ortak.extend(last_two)
        if len(df1.columns) == len(df2.columns):

            return df_den.loc[:, ortak].join(df2.iloc[:, -2:])
        else:
            fark = len(df2.columns) - len_ortak
            return df_den.loc[:, ortak].join(df2.iloc[:, -fark:])

    def sacma(self, list1, list2):
        if list1 and not list2:
            list2.append(self.concat_list(list1[0], list1[1]))
            del list1[:2]
            return self.sacma(list1, list2)
        elif list1 and list2:
            list2.append(self.concat_list(list1[0], list2[-1]))
            del list1[0]
            del list2[0]
            return self.sacma(list1, list2)
        elif not list1 and list2:
            return list2
        else:
            print("Houston, we have a problem")

    def zipper(self, txt, vcf):
        return list(zip(txt, vcf))

    def search_key(self, df, key):
        return df[df.apply(lambda row: row.astype(str).str.contains(key, flags=re.IGNORECASE).any(), axis=1)]

    def filter_type(self, df, type_of, column):
        return df[df[column] == type_of]

    def gene_search_to_csv(self, df, outname, genes):
        df[df["Gene.refGene"].isin(genes) |
           df["Gene.knownGene"].isin(genes) |
           df["Gene.ensGene"].isin(genes)].to_csv(outname, sep="\t", index=False)

    def loh_merges(self, hasta):
        output_list = []
        for i in ["SNP", "INDEL"]:
            main_folder = hasta + "/" + i
            os.chdir(main_folder)
            file_list = glob.glob("*.vcf")
            output_f = self.outputer(file_list[0])
            variants_str = self.list_input_arguments(file_list)
            self.loh_get_het(glob.glob("*LOH*.vcf")[0])
            str_to_run = "java -jar " + self.get_paths.gatk_path + " -T CombineVariants -R " + self.ref_dir + " " + \
                         variants_str + " -o {v_output} --genotypemergeoption UNSORTED".format(v_output=main_folder+"/"+output_f)
            os.system(str_to_run)
            output_list.append(main_folder+"/"+output_f)

        variants_str1 = self.list_input_arguments(output_list)
        str_to_run = "java -jar " + self.get_paths.gatk_path + " -T CombineVariants -R " + self.ref_dir + " " + \
                     variants_str1 + " -o {v_output} --genotypemergeoption UNSORTED".format(v_output=hasta + "/" + output_f)
        os.system(str_to_run)

    def loh_get_het(self, file):
        try:
            data = ""
            with open(file) as f:
                for line in f:
                    if line[0] != "#":
                        tumor = line.split("\t")[10]
                        if tumor[:3] == "1/1":
                            data += line
                        else:
                            pass
                    else:
                        data += line
            os.remove(file)
            with open(file, "w") as f:
                f.write(data)
        except:
            pass


    def list_input_arguments(self, file_list):
        variants_list = ["--variant " + a for a in file_list]
        variants_str = " ".join(variants_list)
        variants_str = " " + variants_str
        return variants_str


    def list_all(self, snp_folder, indel_folder):
        tmp = os.getcwd()
        os.chdir(snp_folder)
        snps = sorted(glob.glob("*.vcf"))
        #snps_l = [snp_folder + "/" + a for a in snps]
        os.chdir(indel_folder)
        indels = sorted(glob.glob("*.vcf"))
        os.chdir(tmp)
        return zip(indels,snps)


    def outputer(self, filename):
        return "_".join(filename.split("_")[2:5])+".vcf"

# folder_list = ["/home/bioinformaticslab/Desktop/merge_loh_somatic/SNP",
#                "/home/bioinformaticslab/Desktop/merge_loh_somatic/INDEL"
#                ]

# for folder in folder_list:
#     print(folder)
#     s1 = prel_analysis(folder)
#     s1.take_func(folder)

#folder = "/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta2/t15"

#folder_list = ["/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/h1"]


fold_list = ["/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta2/s43",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta2/s42",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta3/s44",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta3/s45",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta3/t19",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta4/s47",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta4/t13",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta4/t25",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta7/t21",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta7/t22",
"/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Documents/tree_deneme/t_analysis/sahinfail/hasta7/t23"]

for folder in fold_list:
    s1 = prel_analysis(folder)
    s1.loh_merges(folder)

    annotate = variant_annotation.VariantAnnotation(variant_annotater="Annovar", thread_v="4", wd=folder, sample_name="S37", will_annotate=[], annotate_all=True)

    annotate.run_annotation()