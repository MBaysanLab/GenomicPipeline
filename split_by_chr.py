import glob
import os

from log_command import log_command
from paths import GetPaths


def split_bam_by_chr(file):
    split_command = (
        "for file in " + file + "; "
        'do filename=`echo $file | cut -d "." -f 1`; '
        "for chrom in `seq 1 22` X Y; do "
        "samtools view -bh $file chr${chrom} > ${filename}_Chr_${chrom}.bam; done; done"
    )
    print(split_command)
    log_command(split_command, "split by chrommose", 0)
    all_chr_files = glob.glob("*_Chr_*.bam")
    return all_chr_files


def get_bam_by_chr():
    all_chr_files = glob.glob("*_Chr_*.bam")
    chr_list = {str(a): [] for a in range(1, 23)}
    chr_list["X"] = []
    chr_list["Y"] = []
    for chr_files in all_chr_files:
        if chr_files[-5] == "X":
            chr_list["X"].append(chr_files)
        elif chr_files[-5] == "Y":
            chr_list["Y"].append(chr_files)
        else:
            index_start = chr_files.find("_Chr_") + 5
            chr_a = chr_files[index_start:-4]
            chr_list[chr_a].append(chr_files)
    return chr_list
