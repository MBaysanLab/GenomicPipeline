import pandas as pd
import numpy as np
from itertools import product, chain
from collections import defaultdict

def get_data(path):
    columns_ = ""
    data = []
    with open(path) as f:
        columns_ = f.readline()
        for line in f:
            data.append(line.split("\t"))
    columns_ = columns_.split("\t")
    if len(columns_) != 167:
        columns_.extend([a for a in range(len(columns_), 167, 1)])
    df = pd.DataFrame(data, columns=columns_)
    function_count = dict(df["Func.refGene"].value_counts())
    exonicfunc_count = dict(df["ExonicFunc.refGene"].value_counts())
    function_count = {"Func." + key: value for key, value in function_count.items()}
    exonicfunc_count = {"ExonicFunc." + key: value for key, value in exonicfunc_count.items()}
    return len(df), function_count, exonicfunc_count



def sum_all(a, b):
    c_0 = a[0] + b[0]
    c_1 = defaultdict(list)
    for k, v in chain(a[1].items(), b[1].items()):
        c_1[k].append(sum(list(v)))
    c_2 = defaultdict(list)
    for k, v in chain(a[2].items(), b[2].items()):
        c_2[k].append(sum(list(v)))

    return c_0, c_1, c_2

def finalize_row_data(my_dict):
    valueall_list = []
    for key, value in my_dict.items():
        valueall = {"Sample": key.split("_")[1], "Sample_Map_VariantCaller": key, "TotalVariant": value[0]}
        valueall = dict(valueall, **value[1])
        valueall = dict(valueall, **value[2])

        valueall_list.append(valueall)

    return pd.DataFrame(valueall_list)

def create_stats(main_path, list_of_sample_id, list_of_mapper, list_of_vcaller):
    new_list = list(product(list_of_sample_id, list_of_mapper, list_of_vcaller))
    samples = {}
    if main_path[-1] != "/":
        main_path = main_path + "/"

    to_path = main_path + "stats_output.txt"
    for sample, map, var in new_list:
        if sample[:7] == "Sample_":
            new_sample = sample[7:]
        else:
            new_sample = sample

        my_id = sample + "_" + map + "_" + var
        print(my_id)

        path = main_path + sample + "/" + map + "/" + var + "/Annovar/Annovar_SNP_" + map + "_" + var + "_" + new_sample + ".hg38_multianno.txt"
        s1 = get_data(path)
        samples[my_id] = s1



    write_data = finalize_row_data(samples)
    write_data.to_csv(to_path, index=False, sep="\t")

    return write_data

def create_vcf_dataset(main_path, list_of_sample_id, list_of_mapper, list_of_vcaller):
    new_list = list(product(list_of_sample_id, list_of_mapper, list_of_vcaller))
    samples = []
    if main_path[-1] != "/":
        main_path = main_path + "/"

    for sample, map, var in new_list:
        if sample[:7] == "Sample_":
            new_sample = sample[7:]
        else:
            new_sample = sample

        my_id = sample + "_" + map + "_" + var
        print(my_id)
        if var == "Mutect2":
            path = main_path + sample + "/" + map + "/" + var + "/SNP_" + map + "_" + var + "_" + new_sample + ".vcf"
        elif var == "Varscan":
            path = main_path + sample + "/" + map + "/" + var + "/SNP_" + map + "_" + var + "_" + new_sample + ".Somatic.vcf"
        else:
            path = main_path + sample + "/" + map + "/" + var + "/SNP_" + map + "_" + var + "_" + new_sample + ".vcf"
        s1 = get_vcf_data(path, new_sample, map, var)
        samples.append(s1)

    to_path = main_path + "MergedSamplesByVCF.csv"
    write_data = finalize_vcf_data(samples)
    write_data = write_data[["SampleComb", "CHROM_POS_REF_ALT", "NORMAL_RefDepth", "NORMAL_AllDepth", "TUMOR_RefDepth", "TUMOR_AllDepth", "Sample", "Mapping", "VariantCaller"]]
    write_data.to_csv(to_path, index=False, sep="\t")

def finalize_vcf_data(samples):
    main_df = pd.DataFrame(samples[0])

    for i in range(1, len(samples), 1):
        sample_df = pd.DataFrame(samples[i])
        main_df = pd.concat([main_df, sample_df])

    return main_df

def get_vcf_data(given_path, sample, map, var):
    data = []

    with open(given_path) as f:
        for line in f:
            # outline_dict = {"CHROM_POS_REF_ALT": "", "NORMAL_RefDepth": "", "NORMAL_AllDepth": "", "TUMOR_RefDepth": "", "TUMOR_AllDepth": "", "SampleComb":""}
            if var == "Mutect2":
                if line[:2] == "##":
                    if line[:14] == "##tumor_sample":
                        tumor_sample = line.split("=")[1].replace("\n", "")
                    elif line[:15] == "##normal_sample":
                        normal_sample = line.split("=")[1].replace("\n", "")
                else:
                    if line[0] != "#":
                        current_line = line.split("\t")
                        snv = "{chr}_{pos}_{ref}_{alt}".format(chr=current_line[0], pos=current_line[1],
                                                               ref=current_line[3], alt=current_line[4])
                        format_s = current_line[-3].split(":")
                        if tumor_sample < normal_sample:
                            normal_column = current_line[-1].split(":")
                            tumor_column = current_line[-2].split(":")
                        else:
                            normal_column = current_line[-2].split(":")
                            tumor_column = current_line[-1].split(":")
                        normal_column_values = {format_s[a]:normal_column[a] for a in range(len(format_s))}
                        tumor_column_values = {format_s[a]: tumor_column[a] for a in range(len(format_s))}
                        normal_ad = normal_column_values["AD"].split(",")
                        tumor_ad = tumor_column_values["AD"].split(",")
                        sample_comb = "{}_{}_{}".format(sample, map, var)
                        outline_dict = {"CHROM_POS_REF_ALT": snv, "NORMAL_RefDepth": normal_ad[0], "NORMAL_AllDepth": normal_ad[1],
                                        "TUMOR_RefDepth": tumor_ad[0], "TUMOR_AllDepth": tumor_ad[1], "SampleComb": sample_comb,
                                        "Sample": sample, "Mapping": map, "VariantCaller": var}

                        data.append(outline_dict)

            elif var == "Strelka":

            else:
                if line[0] != "#":
                    current_line = line.split("\t")
                    snv = "{chr}_{pos}_{ref}_{alt}".format(chr=current_line[0], pos=current_line[1],
                                                           ref=current_line[3], alt=current_line[4])
                    format_s = current_line[-3].split(":")
                    normal_column = current_line[-2].split(":")
                    tumor_column = current_line[-1].split(":")
                    normal_column_values = {format_s[a]: normal_column[a] for a in range(len(format_s))}
                    tumor_column_values = {format_s[a]: tumor_column[a] for a in range(len(format_s))}
                    sample_comb = "{}_{}_{}".format(sample, map, var)
                    outline_dict = {"CHROM_POS_REF_ALT": snv, "NORMAL_RefDepth": normal_column_values["RD"],
                                    "NORMAL_AllDepth": normal_column_values["AD"], "TUMOR_RefDepth": tumor_column_values["RD"],
                                    "TUMOR_AllDepth": tumor_column_values["AD"], "SampleComb": sample_comb,
                                        "Sample": sample, "Mapping": map, "VariantCaller": var}

                    data.append(outline_dict)

    return data




samples = ["Sample_NOB0"+str(a) for a in range(2, 9, 1)]
samples.append("Sample_NB09")
samples.extend(["Sample_NB"+str(a) for a in range(10, 33, 1)])
samples.extend(["Sample_NOB"+str(a) for a in range(33, 45, 1)])
samples.extend(["Sample_NOB"+str(a) for a in range(61, 69, 1)])


create_vcf_dataset("/media/bioinformaticslab/Seagate Backup Plus Drive/Ambry/203", samples, ["Bwa", "Bowtie2"], ["Strelka"])


#create_vcf_dataset("/home/bioinformaticslab/Desktop/test files", ["Sample_NOB02"], ["Bwa", "Bowtie2"], ["Mutect2", "Varscan"])