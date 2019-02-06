import os, glob
from gatk_pre_processing import GatkPreProcessing
from run_pipeline_mapping import callmapping
from run_pipeline_variant_calling import call_variant_caller
from variant_annotation import VariantAnnotation



#################### Mapping Codes #########################

#
# folder_list = [("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_42/", "Tumor", "Bwa", "4"),
#                 ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_42/", "Tumor", "Bowtie2", "4"),
#                 ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_43/", "Tumor", "Bwa", "4"),
#                 ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_43/", "Tumor", "Bowtie2", "4"),
#                 ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_44/", "Tumor", "Bwa", "4"),
#                 ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_44/", "Tumor", "Bowtie2", "4"),
#                 ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_45/", "Tumor", "Bwa", "4"),
#                 ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_45/", "Tumor", "Bowtie2", "4"),
#                ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_48/", "Tumor", "Bwa", "4"),
#                ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_48/", "Tumor", "Bowtie2", "4")]
#

# for folder, sampletype, maptype,libr in folder_list:
#     callmapping(working_directory=folder,
#                 var_maptype=maptype, var_sampletype=sampletype, library=libr, threads="4", var_gatk_tools="Yes",
#                 issplitchr="No", trim="Yes", middle_files="No")

#################### Variant Calling Codes #########################

# folde_list = [
#               ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_37/Bowtie2/MergedPreProcess/PreProcess", "S37",  "Bowtie2", "Varscan",
#                "Bowtie2_37_MergedBAM.bam")]
#
# for folder, s_name, map_type, caller, bam in folde_list:
#     if map_type == "Bwa":
#         gm = "/home/selcuk/Desktop/Samples/Sample_40/Bwa/MergedPreProcess/Bwa_40_MergedBAM.bam"
#     else:
#         gm = "/home/selcuk/Desktop/Samples/Sample_40/Bowtie2/MergedPreProcess/Bowtie2_40_MergedBAM.bam"
#     call_variant_caller(var_variantcaller=caller, threads_p=6, var_maptype=map_type,
#                         germline_bam=gm,
#                         working_directory=folder,
#                         tumor_bam=bam, s_name=s_name, tumor_only="No")



#################### Annotation Codes #########################

folde_list = [("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_47/Bwa/MergedPreProcess", "S47"),
                ("/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_47/Bowtie2/MergedPreProcess", "S47")]


for folder, s_name in folde_list:
    f_mutect = folder + "/Mutect2"
    # f_varscan= folder + "/Varscan"

    annotate = VariantAnnotation(variant_annotater="Annovar", thread_v=6, wd=f_mutect, sample_name=s_name,
                                 will_annotate=[""], annotate_all=True)

    annotate.run_annotation()
    # annotate = VariantAnnotation(variant_annotater="Annovar", thread_v=6, wd=f_varscan, sample_name=s_name,
    #                              will_annotate=[""], annotate_all=True)
    #
    # annotate.run_annotation()
    #
