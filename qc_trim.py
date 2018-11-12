import os
import glob
from log_command import log_command
from paths import GetPaths
import re
import gzip
import shutil



def QcTrim(working_directory):
    paths = GetPaths.fastqc
    all_fastq_files = glob.glob("*fastq.gz")
    

