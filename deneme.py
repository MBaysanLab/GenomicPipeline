from shutil import copyfile
import tarfile
import os
from log_command import log_command

source_list1 = [ "/home/bioinformaticslab/Desktop/AMBRY/203/Sample_NB"+str(a)+"/Bwa" for a in range(10,33,1)]
source_list2 = [ "/home/bioinformaticslab/Desktop/AMBRY/203/Sample_NOB"+str(a)+"/Bwa" for a in range(33,69,1)]


dest_list1 = [ "/media/bioinformaticslab/sahin_hdd/Ambry/Sample_NB"+str(a) for a in range(10,33,1)]
dest_list2 = [ "/media/bioinformaticslab/sahin_hdd/Ambry/Sample_NOB"+str(a) for a in range(33,69,1)]


#"sudo mv /home/bioinformaticslab/Desktop/AMBRY/203/Sample_NB10/Bwa/ /media/bioinformaticslab/sahin_hdd/Ambry/Sample_NB10"

for a in range(len(source_list2)):
    command = "sudo mv " + source_list2[a] + " " + dest_list2[a]
    print(command)
#    log_command(command, "move", "0", "move")

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