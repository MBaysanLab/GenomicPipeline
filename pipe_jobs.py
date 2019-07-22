import os, glob, shutil
from gatk_pre_processing import GatkPreProcessing
from run_pipeline_mapping import callmapping
from run_pipeline_variant_calling import call_variant_caller
from variant_annotation import VariantAnnotation



#################### Mapping Codes #########################
# folder_list = [("sample_path", "Tumor", "Bwa", "1")
#                ]
#
#
# for folder, sampletype, maptype,libr in folder_list:
#     callmapping(working_directory=folder,
#             var_maptype=maptype, var_sampletype=sampletype, library=libr, threads="6", var_gatk_tools="Yes",
#             issplitchr="No", trim="Yes", middle_files="No")
#

#################### Variant Calling Codes #########################


# folde_list = [("TumorBamFileFolderPath", "SampleName", "Bwa", "Strelka", "TumorBamFile")]
# for folder, s_name, map_type, caller, bam in folde_list:
#
#     if map_type == "Bwa":
#         gm = "GermlineBamFilePathForBwa"
#     else:
#         gm = "GermlineBamFilePathForOther"
#     call_variant_caller(var_variantcaller=caller, threads_p=4, var_maptype=map_type,
#                         germline_bam=gm,
#                         working_directory=folder,
#                         tumor_bam=bam, s_name=s_name, tumor_only="No")
