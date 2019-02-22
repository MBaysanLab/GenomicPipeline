import variant_calling
import variant_annotation
import split_by_chr as chr


def call_variant_caller(working_directory, tumor_bam, germline_bam, var_maptype, var_variantcaller, threads_p,
                        s_name, tumor_only, tumor_interval=None, germline_interval=None):
    wd = working_directory

    if wd[-1] == "/" or wd[-1] == "\\":
        wd = wd[:-1]

    gm = germline_bam

    if gm[-1] == "/" or gm[-1] == "\\":
        gm = gm[:-1]

    gm_interval = germline_interval

    if gm[-1] == "/" or gm[-1] == "\\":
        gm = gm[:-1]

    tumor_chr_files = chr.split_bam_by_chr(wd + "/" + tumor_bam)

    normal_chr_files = chr.split_bam_by_chr(germline_bam)

    if var_variantcaller == "Mutect2" or var_variantcaller == "Mutect2_gatk3":
        pipeline2 = variant_calling.VariantCall(variant_caller=var_variantcaller, thrds=threads_p, map_type=var_maptype,
                                                germline_bam=gm, germline_interval=gm_interval, wd=wd,
                                                tumor_bam=tumor_bam, tumor_interval=tumor_interval,
                                                sample_name=s_name, tumor_only=tumor_only)
    else:
        pipeline2 = variant_calling.VariantCall(variant_caller=var_variantcaller, thrds=threads_p, map_type=var_maptype,
                                                germline_bam=gm, germline_interval=None, wd=wd, tumor_bam=tumor_bam,
                                                tumor_interval=None, sample_name=s_name,  tumor_only=tumor_only)
    pipeline2_success = pipeline2.run_pipeline()

    annotate = variant_annotation.VariantAnnotation(variant_annotater="Annovar", thread_v=threads_p,
                                                    wd=pipeline2_success, sample_name=s_name, will_annotate=[],
                                                    annotate_all=True)

    annotate.run_annotation()

    return pipeline2_success


if __name__ == "__main__":
    call_variant_caller(var_variantcaller="Mutect2", threads_p=4, var_maptype="Bwa",
                        germline_bam="/home/bioinformaticslab/Desktop/bioinformaticslab/Desktop/AMBRY/DUYGU/Sample_40/Bwa/PreProcess/GATK4_MDUP_Bwa_40_MergedBAM.bam",
                        working_directory="/home/bioinformaticslab/Desktop/testData/Bwa_origin/PreProcess",
                        tumor_bam="GATK4_MDUP_Bwa_37_MergedBAM.bam", s_name="S37", tumor_only="No")

