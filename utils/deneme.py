import os
import shutil

# source_list1 = ["/home/bioinformaticslab/Desktop/AMBRY/203/Sample_NB"+str(a)+"/Bowtie2" for a in range(27,33,1)]
# source_list2 = ["/home/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB"+str(a)+"/Bowtie2" for a in range(33,50,1)]
#
#
# dest_list1 = ["/media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/Bowtie2/Sample_NB"+str(a) for a in range(27,
#                                                                                                                   33,1)]
# dest_list2 = ["/media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/Bowtie2/Sample_NOB"+str(a) for a in range(33,50,1)]
#
#
# #"sudo mv /home/bioinformaticslab/Desktop/AMBRY/203/Sample_NB10/Bwa/ /media/bioinformaticslab/sahin_hdd/Ambry/Sample_NB10"
#
# for a in range(len(source_list2)):
#     command = "sudo mv " + source_list2[a] + " " + dest_list2[a]
#     print(command)
# #    log_command(command, "move", "0", "move")

# for a in range(len(source_list1)):
#     output_filename = source_list1[a].split("/")[-2]
#     src = "/".join(source_list1[a].split("/")[:-1])
#     os.chdir(src)
#     if os.path.exists(src + "/" + output_filename):
#         pass
#     else:
#         with tarfile.open(output_filename, "w:gz") as tar:
#             tar.add(source_list1[a], arcname=os.path.basename(source_list1[a]))
#     dest = "/media/bioinformaticslab/sahin_hdd/Ambry dosyaları/" + output_filename
#     copyfile(src + "/"+output_filename, dest)
#     os.remove(src + "/"+output_filename)
#
# for a in range(len(source_list2)):
#     output_filename = source_list2[a].split("/")[-2]
#     src = "/".join(source_list1[a].split("/")[:-1])
#     os.chdir(src)
#     if os.path.exists(src + "/" + output_filename):
#         pass
#     else:
#         with tarfile.open(output_filename, "w:gz") as tar:
#             tar.add(source_list1[a], arcname=os.path.basename(source_list1[a]))
#     dest="/media/bioinformaticslab/sahin_hdd/Ambry dosyaları/" +output_filename
#     copyfile(src + "/"+output_filename, dest)
#     os.remove(src + "/" + output_filename)

#
#
# from glob import glob
#
# import shutil
#
# f_list = [("/media/selcuk/duygu/Sample_t13/Bowtie2/Mutect2/Annovar/", "t13")
#           ]
#
# for a, k in f_list:
#     print(a)
#     os.chdir(a)
#     b_list = glob("*.txt")
#     to_path = "/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/txts/4_Hasta/" + k
#     print(to_path)
#     try:
#         os.mkdir(to_path)
#     except:
#         pass
#     for b in b_list:
#         shutil.copy(a + "/" + b, to_path + "/" + b)
#         print(b)
#     b_list = glob("*.vcf")
#     for b in b_list:
#         shutil.copy(a + "/" + b, to_path + "/" + b)
#         print(b)

# import os
# from glob import glob
# liste = ["/home/selcuk/Desktop/Samples/Bowtie2/Project_190123_D00425_0263_DUYGU/Sample_d7E/",
#          "/home/selcuk/Desktop/Samples/Bowtie2/Project_190123_D00425_0263_DUYGU/Sample_t14/",
#          "/home/selcuk/Desktop/Samples/Bowtie2/Project_190123_D00425_0263_DUYGU/Sample_t16/",
#          "/home/selcuk/Desktop/Samples/Bowtie2/Project_190123_D00425_0263_DUYGU/Sample_t26/"]
#
# for l in liste:
#     os.chdir(l)
#     print(l)
#     for filename in os.listdir("."):
#         if not filename.endswith(".csv"):
#             os.rename(filename, filename[:3] + "_GermlineDNA" + filename[3:])



# commands = ["mkdir -p /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB0" + str(a) + "/Bowtie2/PreProcess/" for a in range(2, 9, 1)]
# commands.extend(["mkdir -p /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NB0" + str(a) + "/Bowtie2/PreProcess/" for a in range(9, 10, 1)])
# commands.extend(["mkdir -p /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NB" + str(a) + "/Bowtie2/PreProcess/" for a in range(10, 33, 1)])
# commands.extend(["mkdir -p /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess/" for a in range(33, 45, 1)])
# commands.extend(["mkdir -p /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess/" for a in range(61, 69, 1)])


# commands = ["cp -R /media/bioinformaticslab2/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB0" + str(a) + "/Bowtie2/PreProcess/ /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB0" + str(a) + "/Bowtie2/PreProcess/" for a in range(2, 9, 1)]
# commands.extend(["cp -R /media/bioinformaticslab2/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NB0" + str(a) + "/Bowtie2/PreProcess/ /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NB0" + str(a) + "/Bowtie2/PreProcess/" for a in range(9, 10, 1)])
# commands.extend(["cp -R /media/bioinformaticslab2/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NB" + str(a) + "/Bowtie2/PreProcess/ /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NB" + str(a) + "/Bowtie2/PreProcess/" for a in range(10, 33, 1)])
# commands.extend(["cp -R /media/bioinformaticslab2/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess/ /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess/" for a in range(33, 45, 1)])
# commands.extend(["cp -R /media/bioinformaticslab2/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess/ /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess/" for a in range(61, 69, 1)])



commands = ["mv /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB0" + str(a) + "/Bowtie2/PreProcess/PreProcess /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB0" + str(a) + "/Bowtie2/PreProcess" for a in range(2, 9, 1)]
commands.extend(["mv /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NB0" + str(a) + "/Bowtie2/PreProcess/PreProcess /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NB0" + str(a) + "/Bowtie2/PreProcess" for a in range(9, 10, 1)])
commands.extend(["mv /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NB" + str(a) + "/Bowtie2/PreProcess/PreProcess /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NB" + str(a) + "/Bowtie2/PreProcess" for a in range(10, 33, 1)])
commands.extend(["mv /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess/PreProcess /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess" for a in range(33, 45, 1)])
commands.extend(["mv /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess/PreProcess /home/bioinformaticslab2/Desktop/Ambry/203/Sample_NOB" + str(a) + "/Bowtie2/PreProcess" for a in range(61, 69, 1)])

# commands.extend(["mv /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB0" + str(a) + "/Bwa/Strelka/Strelka2_INDEL_NOB0"+str(a)+".vcf /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB0" + str(a) + "/Bwa/Strelka/INDEL_Bwa_Strelka2_NOB0"+str(a)+".vcf" for a in range(2, 9, 1)])
# commands.extend(["mv /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NB0" + str(a) + "/Bwa/Strelka/Strelka2_INDEL_NB0"+str(a)+".vcf /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NB0" + str(a) + "/Bwa/Strelka/INDEL_Bwa_Strelka2_NB0"+str(a)+".vcf" for a in range(9, 10, 1)])
# commands.extend(["mv /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NB" + str(a) + "/Bwa/Strelka/Strelka2_INDEL_NB"+str(a)+".vcf /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NB" + str(a) + "/Bwa/Strelka/INDEL_Bwa_Strelka2_NB"+str(a)+".vcf" for a in range(10, 33, 1)])
# commands.extend(["mv /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB" + str(a) + "/Bwa/Strelka/Strelka2_INDEL_NOB"+str(a)+".vcf /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB" + str(a) + "/Bwa/Strelka/INDEL_Bwa_Strelka2_NOB"+str(a)+".vcf" for a in range(33, 45, 1)])
# commands.extend(["mv /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB" + str(a) + "/Bwa/Strelka/Strelka2_INDEL_NOB"+str(a)+".vcf /media/bioinformaticslab/Seagate\ Backup\ Plus\ Drive/Ambry/203/Sample_NOB" + str(a) + "/Bwa/Strelka/INDEL_Bwa_Strelka2_NOB"+str(a)+".vcf" for a in range(61, 69, 1)])


for c in commands:
    print(c)

# folder = "/home/selcuk/Desktop/Somatic/Bwa/"
# path_dest1 = "/media/selcuk/duygu/" + folder.split("/")[-3]
# path_dest2 = path_dest1 + "/" + folder.split("/")[-2] + "/"
# if not os.path.exists(path_dest1):
#     os.mkdir(path_dest1)
#
#
#
#
# # dosya kopyalama





#
# import os
# file_list = ["/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_42",
#           "/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_43",
#           "/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_44",
#           "/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_45",
#              "/media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/Data/Sample_48"]
#
# for file in file_list:
#     fs = ["Bwa", "Bowtie2"]
#     for f in fs:
#         folder_b = file + "/" + f
#         os.chdir(folder_b)
#         os.mkdir("MergedPreProcess")
#         os.chdir(folder_b + "/MergedPreProcess")
#         os.mkdir("PreProcess")

#
# import os
#
# commands = ["java -jar /home/selcuk/Desktop/paths/GenomeAnalysisTK.jar -nct 4 -R /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/Homo_sapiens_assembly38.fasta -T HaplotypeCaller -I /media/selcuk/duygu/Sample_t24/Bwa/PreProcess/GATK4_MDUP_Bwa_t24_MergedBAM.bam --dbsnp /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/dbsnp_146.hg38.vcf.gz -o /media/selcuk/duygu/Sample_t24/Bwa/PreProcess/GATK4_MDUP_Bwa_t24_MergedBAM.raw.snps.indels.vcf",
#             "java -jar /home/selcuk/Desktop/paths/GenomeAnalysisTK.jar -nct 4 -R /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/Homo_sapiens_assembly38.fasta -T HaplotypeCaller -I /media/selcuk/duygu/Sample_t26/Bwa/PreProcess/GATK4_MDUP_Bwa_t26_MergedBAM.bam --dbsnp /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/dbsnp_146.hg38.vcf.gz -o /media/selcuk/duygu/Sample_t26/Bwa/PreProcess/GATK4_MDUP_Bwa_t26_MergedBAM.raw.snps.indels.vcf",
#             "java -jar /home/selcuk/Desktop/paths/GenomeAnalysisTK.jar -nct 4 -R /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/Homo_sapiens_assembly38.fasta -T HaplotypeCaller -I /media/selcuk/duygu/Sample_t16/Bwa/PreProcess/GATK4_MDUP_Bwa_t16_MergedBAM.bam --dbsnp /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/dbsnp_146.hg38.vcf.gz -o /media/selcuk/duygu/Sample_t16/Bwa/PreProcess/GATK4_MDUP_Bwa_t16_MergedBAM.raw.snps.indels.vcf",
#             "java -jar /home/selcuk/Desktop/paths/GenomeAnalysisTK.jar -nct 4 -R /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/Homo_sapiens_assembly38.fasta -T HaplotypeCaller -I /media/selcuk/duygu/Sample_t14/Bwa/PreProcess/GATK4_MDUP_Bwa_t14_MergedBAM.bam --dbsnp /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/dbsnp_146.hg38.vcf.gz -o /media/selcuk/duygu/Sample_t14/Bwa/PreProcess/GATK4_MDUP_Bwa_t14_MergedBAM.raw.snps.indels.vcf",
#             "java -jar /home/selcuk/Desktop/paths/GenomeAnalysisTK.jar -nct 4 -R /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/Homo_sapiens_assembly38.fasta -T HaplotypeCaller -I /media/selcuk/duygu/Sample_t24/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_t24_MergedBAM.bam --dbsnp /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/dbsnp_146.hg38.vcf.gz -o /media/selcuk/duygu/Sample_t24/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_t24_MergedBAM.raw.snps.indels.vcf",
#             "java -jar /home/selcuk/Desktop/paths/GenomeAnalysisTK.jar -nct 4 -R /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/Homo_sapiens_assembly38.fasta -T HaplotypeCaller -I /media/selcuk/duygu/Sample_t26/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_t26_MergedBAM.bam --dbsnp /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/dbsnp_146.hg38.vcf.gz -o /media/selcuk/duygu/Sample_t26/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_t26_MergedBAM.raw.snps.indels.vcf",
#             "java -jar /home/selcuk/Desktop/paths/GenomeAnalysisTK.jar -nct 4 -R /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/Homo_sapiens_assembly38.fasta -T HaplotypeCaller -I /media/selcuk/duygu/Sample_t16/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_t16_MergedBAM.bam --dbsnp /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/dbsnp_146.hg38.vcf.gz -o /media/selcuk/duygu/Sample_t16/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_t16_MergedBAM.raw.snps.indels.vcf",
#             "java -jar /home/selcuk/Desktop/paths/GenomeAnalysisTK.jar -nct 4 -R /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/Homo_sapiens_assembly38.fasta -T HaplotypeCaller -I /media/selcuk/duygu/Sample_t14/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_t14_MergedBAM.bam --dbsnp /media/selcuk/a58b0f32-9a6f-41f5-b0b2-ff63351982fd/hg38_bundle/dbsnp_146.hg38.vcf.gz -o /media/selcuk/duygu/Sample_t14/Bowtie2/PreProcess/GATK4_MDUP_Bowtie2_t14_MergedBAM.raw.snps.indels.vcf"]
#
# try:
#     for c in commands:
#         os.system(c)
# except:
#     pass
