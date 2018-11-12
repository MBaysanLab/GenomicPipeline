import os
import glob
from log_command import log_command
from paths import GetPaths
import re
import gzip
import shutil


def get_fastq(trimmed=False):
    """
    Get fastq files names with their extension

    Returns
    -------
    list
        A list of fastq files inside of given working directory.

    """
    if trimmed == False:
        all_fastq_files = glob.glob("*fastq.gz")
        split_names_v = [os.path.splitext(os.path.splitext(i)[0])[0] for i in all_fastq_files]
        return split_names_v
    else:
        all_fastq_files = glob.glob("*fastq.gz")
        split_names_v = [os.path.splitext(os.path.splitext(i)[0])[0] for i in all_fastq_files]
        split_names_trim = ["_".join(i.split("_")[1:]) for i in split_names_v]
        return split_names_trim


def get_info(sample_type, fastq_list):

    """
    Prepare set of information in order to use next steps especially creating read group in mapping function.

    Returns
    -------
    dict
        list of unique information inside dictionary
    """
    sample_id, germline_dna, index_seq, lanes, pairs_r, n_of_seq = (set() for i in range(6))
    if sample_type == "Tumor":
        for i in fastq_list:
            sample_id.add(i.split("_")[0])
            index_seq.add(i.split("_")[1])
            lanes.add(i.split("_")[2])
            pairs_r.add(i.split("_")[3])
            n_of_seq.add(i.split("_")[4])

        list_with_info = {"Sample_ID": list(sample_id), "Index": list(index_seq), "Lanes": list(lanes),
                          "Pairs": list(pairs_r), "Number_of_seq": list(n_of_seq)}
        return list_with_info
    elif sample_type == "Germline" or sample_type == "Normal":

        for i in fastq_list:
            sample_id.add(i.split("_")[0])
            germline_dna.add(i.split("_")[1])
            index_seq.add(i.split("_")[2])
            lanes.add(i.split("_")[3])
            pairs_r.add(i.split("_")[4])
            n_of_seq.add(i.split("_")[5])

        list_with_info = {"Sample_ID": list(sample_id), "Germline": list(germline_dna), "Index": list(index_seq),
                          "Lanes": list(lanes), "Pairs": list(pairs_r), "Number_of_seq": list(n_of_seq)}
        return list_with_info
    else:
        print("raise error and ask again for a valid sample type")


def create_folder(working_directory, all_files, map_type=None, first=False, step="Master", folder_directory=None):
    if first:
        all_files.append("log_file.txt")
        mk_dir = working_directory + "/" + map_type
        os.mkdir(mk_dir)
        mk_dir += "/" + step
        os.mkdir(mk_dir)
        for file in all_files:
            if file[-2:] != "gz":
                print("mapping crate folder print " + file)
                shutil.move(working_directory + "/" + file, mk_dir + "/" + file)

    else:
        all_files.append("log_file.txt")
        mk_dir = folder_directory + "/" + step
        os.mkdir(mk_dir)
        for file in all_files:
            if file[-2:] != "gz":
                print("preprocess crate folder print " + file)
                shutil.move(working_directory + "/" + file, mk_dir + "/" + file)


def create_index(lastbam, function, threads, step):
    indexcol = "java -jar " + GetPaths().picard_path + " BuildBamIndex I=" + lastbam
    log_command(indexcol, function, threads, step)
    return lastbam[:-3] + "bai"


os.chdir("/home/bioinformaticslab/Desktop/AMBRY/DUYGU_1/Sample_37/trimmed")
a = get_fastq(trimmed=True)

