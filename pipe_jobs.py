import os, glob
from gatk_pre_processing import GatkPreProcessing
from run_pipeline_mapping import callmapping
from run_pipeline_variant_calling import call_variant_caller
from variant_annotation import VariantAnnotation



#################### Mapping Codes #########################


folder_list = [("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB01_GermlineDNA", "Germline", "Bwa", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB03", "Tumor", "Bwa", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB04", "Tumor", "Bwa", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB05", "Tumor", "Bwa", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB06", "Tumor", "Bwa", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB07", "Tumor", "Bwa", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB08", "Tumor", "Bwa", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB01_GermlineDNA", "Germline", "Bowtie2", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB03", "Tumor", "Bowtie2", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB04", "Tumor", "Bowtie2", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB05", "Tumor", "Bowtie2", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB06", "Tumor", "Bowtie2", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB07", "Tumor", "Bowtie2", "1"),
               ("/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB08", "Tumor", "Bowtie2", "1"),
               ]


for folder, sampletype, maptype,libr in folder_list:
    callmapping(working_directory=folder,
                var_maptype=maptype, var_sampletype=sampletype, library=libr, threads="6", var_gatk_tools="Yes",
                issplitchr="No", trim="Yes", middle_files="No")

#################### Variant Calling Codes #########################

# folde_list = [
#               ("/home/bioinformaticslab/Desktop/batu/deneme/37_d/Bwa/PreProcess", "S37d",  "Bwa", "Mutect2",
#                "GATK4_MDUP_Bwa_37_MergedBAM.bam")]
#
# for folder, s_name, map_type, caller, bam in folde_list:
#     if map_type == "Bwa":
#         gm = "/home/bioinformaticslab/Desktop/batu/deneme/40_d/Bwa/PreProcess/GATK4_MDUP_Bwa_40_MergedBAM.bam"
#     else:
#         gm = "/home/bioinformaticslab/Desktop/batu/deneme/40_d/Bwa/PreProcess/GATK4_MDUP_Bwa_40_MergedBAM.bam"
#     call_variant_caller(var_variantcaller=caller, threads_p=6, var_maptype=map_type,
#                         germline_bam=gm,
#                         working_directory=folder,
#                         tumor_bam=bam, s_name=s_name, tumor_only="No")



#################### Annotation Codes #########################

# folde_list = [("/home/bioinformaticslab/Desktop/batu/deneme/37_d/Bwa", "S37d")]
#
#
# for folder, s_name in folde_list:
#     #f_mutect = folder + "/Mutect2"
#     f_varscan= folder + "/Varscan"
#
#     #annotate = VariantAnnotation(variant_annotater="Annovar", thread_v=6, wd=f_mutect, sample_name=s_name,
#      #                            will_annotate=[""], annotate_all=True)
#
#     #annotate.run_annotation()
#     annotate = VariantAnnotation(variant_annotater="Annovar", thread_v=6, wd=f_varscan, sample_name=s_name,
#                                  will_annotate=[""], annotate_all=True)
#
#     annotate.run_annotation()
#
