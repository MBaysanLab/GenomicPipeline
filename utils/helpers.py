import os
import glob
from utils.log_command import log_command
from paths import GetPaths
import shutil
import gzip
import subprocess
import tempfile


def get_fastq():
    """
    Get fastq files names with their extension

    Returns
    -------
    list
        A list of fastq files inside of given working directory.
    """

    all_fastq_files = glob.glob("*fastq.gz")
    split_names_v = [os.path.splitext(os.path.splitext(i)[0])[0] for i in all_fastq_files]
    return split_names_v


def get_info(sample_type, fastq_list, trimmed=False):

    """
    Prepare set of information in order to used in next steps especially creating read group in mapping function.

    Returns
    -------
    dict
        list of unique information inside dictionary
    """
    sample_id, germline_dna, index_seq, lanes, pairs_r, n_of_seq = (set() for i in range(6))
    if sample_type == "Tumor":
        for i in fastq_list:
            if trimmed:
                sample_id.add(i.split("_")[1])
                index_seq.add(i.split("_")[2])
                lanes.add(i.split("_")[3])
                pairs_r.add(i.split("_")[4])
                n_of_seq.add(i.split("_")[5])
            else:
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
            if trimmed:
                sample_id.add(i.split("_")[1])
                germline_dna.add(i.split("_")[2])
                index_seq.add(i.split("_")[3])
                lanes.add(i.split("_")[4])
                pairs_r.add(i.split("_")[5])
                n_of_seq.add(i.split("_")[6])
            else:
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




def create_folder(working_directory, all_files, map_type=None, step="Other", folder_directory=None, master_step=False):
    all_files.append("log_file.txt")
    all_files_set = set(all_files)
    if step == "QC":
        mk_dir = working_directory + "/" + step
        os.mkdir(mk_dir)
        for file in all_files_set:
            shutil.move(working_directory + "/" + file, mk_dir + "/" + file)
    elif step == "Mapping":
        mk_dir = folder_directory + "/" + map_type
        os.mkdir(mk_dir)
        mk_dir += "/" + step
        os.mkdir(mk_dir)
        for file in all_files_set:
            if file[-2:] != "gz":
                shutil.move(working_directory + "/" + file, mk_dir + "/" + file)
    else:
        mk_dir = folder_directory + "/" + step
        os.mkdir(mk_dir)
        for file in all_files_set:
            shutil.move(working_directory + "/" + file, mk_dir + "/" + file)


def delete_files_from_folder(working_directory, map_type, step, file_list):
    os.chdir(working_directory + "/" + map_type + "/" + step)
    file_list_extend = [f.split(".")[0] + ".bai" for f in file_list]
    file_list_extend.extend(file_list)
    all_files = glob.glob("*")
    file_list_extend.append("log_file.txt")
    for file in all_files:
        if os.path.exists(file) and (file not in file_list_extend):
            os.remove(file)
        else:
            pass


def create_index(lastbam, function, threads, step):
    indexcol = "java -Dpicard.useLegacyParser=false -jar " + GetPaths().picard_path + " BuildBamIndex -I " + lastbam
    log_command(indexcol, function, threads, step)
    return lastbam[:-3] + "bai"


def get_sample_name(bamfile):
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

def strelka_move_files(source, destination, case):
    try:
        os.mkdir(destination)
    except:
        pass

    root_src_dir = os.path.join('.', source)
    root_target_dir = os.path.join('.', destination)

    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_folder_value = destination.split("/")[-1]
        if dst_folder_value in dirs:
            dirs.remove(dst_folder_value)
        dst_dir = src_dir.replace(root_src_dir, root_target_dir)
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        for file_ in files:
            if case == 0:
                if "BAM" not in file_:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    if os.path.exists(dst_file):
                        pass
                    shutil.move(src_file, dst_dir)
            elif case == 1:
                if "SNP_" not in file_ and "INDEL_" not in file_ and "log_file.txt" not in file_:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    if os.path.exists(dst_file):
                        pass
                    shutil.move(src_file, dst_dir)
            else:
                pass
    try:
        for dir_ in ["results", "workspace"]:
            shutil.rmtree(source + "/" + dir_)
    except:
        pass


def create_strelka_folder(main_dir, sample_name):

    if main_dir[-1] != "/":
        main_dir = main_dir + "/"
    source_dir = main_dir + "PreProcess"
    os.chdir(source_dir)
    dest_dir = main_dir + "Strelka"
    try:
        os.mkdir(dest_dir)
    except:
        pass

    strelka_move_files(source_dir, dest_dir, 0)

    os.chdir(dest_dir + "/results/variants")

    vcf_files = glob.glob("*.vcf.gz")
    snp_output = "SNP_" + sample_name.split("/")[-1] + ".vcf"
    indel_output = "INDEL_" + sample_name.split("/")[-1] + ".vcf"
    for vcf_file in vcf_files:

        with gzip.open(vcf_file, 'rb') as f_in:
            if "snvs" in vcf_file:
                with open(snp_output, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                    shutil.move(dest_dir + "/results/variants/" + snp_output, dest_dir+"/" + snp_output)
            else:
                with open(indel_output, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                    shutil.move(dest_dir + "/results/variants/" + indel_output, dest_dir + "/" + indel_output)

    os.chdir(dest_dir)
    strelka_move_files(dest_dir, dest_dir+"/"+"MiddleFiles", 1)



#strelka_gt_adder("/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB02/Bwa/Strelka")
# folde_list = []
# folde_list = [("/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB0" +str(a) + "/Bwa/", "NOB0"+str(a)) for a in range(4, 9, 1)]
# #folde_list.append(("/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Desktop/AMBRY/203/Sample_NB09/Bwa/PreProcess", "NB09", "Bwa", "Strelka", "GATK4_MDUP_Bwa_NB09_MergedBAM.bam"))
# folde_list.extend([("/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Desktop/AMBRY/203/Sample_NB"+str(a) + "/Bwa/", "NB"+str(a)) for a in range(10, 33, 1)])
# folde_list.extend([("/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB" +str(a) + "/Bwa/", "NOB"+str(a)) for a in range(33, 45, 1)])
# folde_list.extend([("/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB" +str(a) + "/Bwa/", "NOB"+str(a)) for a in range(61, 69, 1)])
#
# for folde_ in folde_list:
#     print(folde_[0])
#     create_strelka_folder(folde_[0], folde_[1])