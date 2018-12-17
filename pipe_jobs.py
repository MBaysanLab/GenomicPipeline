import os, glob
from gatk_pre_processing import GatkPreProcessing
from run_pipeline_mapping import callmapping
from run_pipeline_variant_calling import call_variant_caller


folder_list = [("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_41", "Tumor", "Bowtie2"),
               ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_40", "Germline", "Bowtie2"),
               ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_39", "Tumor", "Bowtie2"),
               ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_38", "Tumor", "Bowtie2"),
               ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_37", "Tumor", "Bowtie2")]

# folder_list = [("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_37/Bowtie2/PreProcess", "S37", "Bowtie2", "Mutect2",
#                 "GATK4_MDUP_Bowtie2_37_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_38/Bowtie2/PreProcess", "S38", "Bowtie2", "Mutect2",
#                 "GATK4_MDUP_Bowtie2_38_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_39/Bowtie2/PreProcess", "S39", "Bowtie2", "Mutect2",
#                 "GATK4_MDUP_Bowtie2_39_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_41/Bowtie2/PreProcess", "S41", "Bowtie2", "Mutect2",
#                 "GATK4_MDUP_Bowtie2_41_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_37/Bowtie2/PreProcess", "S37", "Bowtie2", "Varscan",
#                 "GATK4_MDUP_Bowtie2_37_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_38/Bowtie2/PreProcess", "S38", "Bowtie2", "Varscan",
#                 "GATK4_MDUP_Bowtie2_38_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_39/Bowtie2/PreProcess", "S39", "Bowtie2", "Varscan",
#                 "GATK4_MDUP_Bowtie2_39_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_41/Bowtie2/PreProcess", "S41", "Bowtie2", "Varscan",
#                 "GATK4_MDUP_Bowtie2_41_MergedBAM.bam")
#                ]

# for folder, sampletype, maptype in folder_list:
#     callmapping(working_directory=folder,
#                 var_maptype=maptype, var_sampletype=sampletype, library="1", threads="2", var_gatk_tools="Yes",
#                 issplitchr="No", trim="Yes")

# for folder, s_name, map_type, caller, bam in folder_list:
#     call_variant_caller(var_variantcaller=caller, threads_p=3, var_maptype=map_type,
#                         germline_bam="/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_40/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_40_MergedBAM.bam",
#                         working_directory=folder,
#                         tumor_bam=bam, s_name=s_name, tumor_only="No")

for folder, sampletype, maptype in folder_list:
    folder_md = folder + "/Bowtie2/PreProcess"
    os.chdir(folder_md)
    print(os.getcwd())
    after_markdpl_file = glob.glob("MDUP_*.bam")
    print(after_markdpl_file)
    gatk_file_list = []
    for file in after_markdpl_file:
        gatk_pre_processing_step = GatkPreProcessing(
            working_directory=folder,
            map_type=maptype, sample_type=sampletype, library_matching_id="1", thrds="4")

        return_files = gatk_pre_processing_step.run_gatks4(file)
        print(return_files)
        gatk_file_list.append(return_files)
        print(gatk_file_list)