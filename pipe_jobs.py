import os, glob
from gatk_pre_processing import GatkPreProcessing
from run_pipeline_mapping import callmapping
from run_pipeline_variant_calling import call_variant_caller
from variant_annotation import VariantAnnotation
import helpers


folder_list = [("/home/bioinformaticslab/Desktop/AMBRY/203/Sample_NB09", "Tumor", "Bowtie2")]
for i in range(10, 33, 1):
    folder_list.append(("/home/bioinformaticslab/Desktop/AMBRY/203/Sample_NB" + str(i), "Tumor", "Bowtie2"))
print(folder_list)
folder_list1 = [("/home/bioinformaticslab/Desktop/AMBRY/Sample_NOB01_GermlineDNA", "Germline", "Bwa"),
                ("/home/bioinformaticslab/Desktop/AMBRY/Sample_NOB01_GermlineDNA", "Germline", "Bowtie2")]
# for sample in folder_list:
#     for i in range(4):
#         if i==0:
#             sample1 = sample + "/Bwa/Varscan/Annovar"
#         elif i==1:
#             sample1 = sample + "/Bwa/Mutect2/Annovar"
#         elif i==2:
#             sample1 = sample + "/Bowtie2/Varscan/Annovar"
#         else:
#             sample1 = sample + "/Bowtie2/Mutect2/Annovar"
#
#         annotate = VariantAnnotation(variant_annotater="Annovar", thread_v=6,
#                                      wd=sample1,
#                                      sample_name="1", will_annotate=[],
#                                      annotate_all=True)
#
#         annotate.run_annotation()



# folder_list = [("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_41", "Tumor", "Bowtie2"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_40", "Germline", "Bowtie2"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_39", "Tumor", "Bowtie2"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_38", "Tumor", "Bowtie2"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_37", "Tumor", "Bowtie2")]
#
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
#               ]

for folder, sampletype, maptype in folder_list:
    callmapping(working_directory=folder,
                var_maptype=maptype, var_sampletype=sampletype, library="1", threads="4", var_gatk_tools="Yes",
                issplitchr="No", trim="Yes", middle_files="No")
#
# for folder, s_name, map_type, caller, bam in folder_list:
#     call_variant_caller(var_variantcaller=caller, threads_p=3, var_maptype=map_type,
#                         germline_bam="/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_40/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_40_MergedBAM.bam",
#                         working_directory=folder,
#                         tumor_bam=bam, s_name=s_name, tumor_only="No")

#
# folde_list = [("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_37/Bwa/PreProcess", "S37", "Bwa", "Mutect2",
#                 "GATK4_MDUP_Bwa_37_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_38/Bwa/PreProcess", "S38", "Bwa", "Mutect2",
#                 "GATK4_MDUP_Bwa_38_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_39/Bwa/PreProcess", "S39", "Bwa", "Mutect2",
#                 "GATK4_MDUP_Bwa_39_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_41/Bwa/PreProcess", "S41", "Bwa", "Mutect2",
#                 "GATK4_MDUP_Bwa_41_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_37/Bwa/PreProcess", "S37", "Bwa", "Varscan",
#                 "GATK4_MDUP_Bwa_37_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_38/Bwa/PreProcess", "S38", "Bwa", "Varscan",
#                 "GATK4_MDUP_Bwa_38_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_39/Bwa/PreProcess", "S39", "Bwa", "Varscan",
#                 "GATK4_MDUP_Bwa_39_MergedBAM.bam"),
#                ("/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_41/Bwa/PreProcess", "S41", "Bwa", "Varscan",
#                 "GATK4_MDUP_Bwa_41_MergedBAM.bam")
#                ]
#
# for folder, s_name, map_type, caller, bam in folde_list:
#     call_variant_caller(var_variantcaller=caller, threads_p=3, var_maptype=map_type,
#                         germline_bam="/home/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_40/Bwa/PreProcess/GATK4_MDUP_Bwa_40_MergedBAM.bam",
#                         working_directory=folder,
#                         tumor_bam=bam, s_name=s_name, tumor_only="No")
#

# for folder, sampletype, maptype in folder_list:
#     folder_md = folder + "/Bowtie2/PreProcess"
#     os.chdir(folder_md)
#     print(os.getcwd())
#     after_markdpl_file = glob.glob("MDUP_*.bam")
#     print(after_markdpl_file)
#     gatk_file_list = []
#     for file in after_markdpl_file:
#         gatk_pre_processing_step = GatkPreProcessing(
#             working_directory=folder,
#             map_type=maptype, sample_type=sampletype, library_matching_id="1", thrds="4")
#
#         return_files = gatk_pre_processing_step.run_gatks4(file)
#         print(return_files)
#         gatk_file_list.append(return_files)
#         print(gatk_file_list)