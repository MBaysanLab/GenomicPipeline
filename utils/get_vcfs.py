from glob import glob
import shutil
import os
from itertools import product


#list of collections
#folder_list = [("source folder path", "Annotation Type (SNP, INDEL)","destination pat" )]


def create_list(main_path, list_of_types ,list_of_sample_id, list_of_mapper, list_of_vcaller, to_path):
    new_list = list(product(list_of_sample_id, list_of_mapper, list_of_vcaller, list_of_types))

    f_list = []
    if main_path[-1] != "/":
        main_path = main_path + "/"

    for sample, mapper, vcaller, types in new_list:
        set_el1 = main_path + sample + "/" + mapper + "/" + vcaller + "/Annovar/"
        set_el2 = types
        set_el3 = to_path

        append_set = (set_el1, set_el2, set_el3)
        f_list.append(append_set)

    collect_txts(f_list)


def collect_txts(f_list):
    for folder_path, folder_name, to_path in f_list:
        print(folder_path)
        os.chdir(folder_path)
        to_path = to_path + folder_name
        print(to_path)

        try:
            os.mkdir(to_path)
        except:
            pass

        a = "Annovar_" + folder_name + "_Bowtie2_Mutect2_*.hg38_multianno*"
        b = "Annovar_" + folder_name + "_Bowtie2_Varscan_*_Somatic.hg38_multianno*"
        c = "Annovar_" + folder_name + "_Bwa_Mutect2_*.hg38_multianno*"
        d = "Annovar_" + folder_name + "_Bwa_Varscan_*_Somatic.hg38_multianno*"

        b_list = []
        b_list.extend(glob(a))
        b_list.extend(glob(b))
        b_list.extend(glob(c))
        b_list.extend(glob(d))

        b_list = set(b_list)
        for b in b_list:
            if os.path.exists(folder_path + "/" + b):
                shutil.copy(folder_path + "/" + b, to_path + "/" + b)
                print(b)
            else:
                pass


samples = ["Sample_NOB"+str(a) for a in range(61,69,1)]
create_list(main_path="/media/bioinformaticslab/Seagate Backup Plus Drive/Ambry/203",
            list_of_sample_id=samples, list_of_mapper=["Bwa", "Bowtie2"], list_of_vcaller=["Mutect2", "Varscan"], list_of_types=["SNP", "INDEL"],
            to_path="/media/bioinformaticslab/369ca485-b3f2-4f04-bbfb-8657aad7669e/bioinformaticslab/Desktop/AMBRY/203/All/" )