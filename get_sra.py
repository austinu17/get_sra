#!/usr/bin/env python 

# add shebang at top of file
# shebang tell the shell how to interpret the file

# Set permission to run file
#    ls -la 
#    chmod ugo+x get_sra.py 
#
import subprocess
import pandas as pd
import sys
import os.path
from shutil import copyfile

if len(sys.argv) ==1:
  print("TOO FEW ARGUMENTS... PLEASE ADD SRR_ACC_LIST.TXT FILE")
  sys.exit(-1)
elif len(sys.argv) >2:
  print("TOO MANY ARGUMENTS... IGNORING EXTRA ARGUMENTS...")
  
if os.path.isfile(sys.argv[1]) == False:
  print("SRR FILE NOT FOUND... EXITING...")                   
  sys.exit(-2)

print("program running")

print("program running")

print(sys.argv)

# open SRR_Acc_list.txt
df = pd.read_csv(sys.argv[1],header=None)

sras = df[0].tolist()

for sra in sras:
    if os.path.isfile(sra+".sra") == True and os.path.isfile(sra+"_tmp.sra") == False:
        print(sra+".sra" " FILE ALREADY DOWNLOADED")
        continue
    ftp_root = "ftp://ftp-trace.ncbi.nih.gov"
    #sra_path = "/sra/sra-instant/reads/ByRun/sra/{SRR|ERR|DRR}/<first 6 characters of accession>/<accession>/<accession>.sra"  
    sra_path = "/sra/sra-instant/reads/ByRun/sra/{}/{}/{}/{}.sra".format(sra[0:3],sra[0:6],sra,sra)
    #print(ftp_root + sra_path)
    exit_status = subprocess.run(['wget','-c' ,'-O',sra+"_tmp.sra",ftp_root + sra_path])
    print(exit_status)
    print(exit_status.returncode)
    if exit_status.returncode == 0:
        os.rename(sra+"_tmp.sra", sra+".sra")
    else:
        print("Did Not Copy")
    if os.path.isfile(sra+".sra") and os.path.isfile(sra+"_tmp.sra") == True:
        os.remove(sra+".sra")
     
for sra in sras:
#SRA File from previous part before, with no Fastq file
    if os.path.isfile(sra+".fastq") == False and os.path.isfile(sra+".sra") == True:
        print("CONVERTING "+ sra+".sra"+ " TO FASTQ FILE...")
        subprocess.run(['fastq-dump',sra + ".sra"])
        os.remove(sra+".sra")
#SRA and Fastq file from failure to commplete fastq download
    elif os.path.isfile(sra+".sra") == True and os.path.isfile(sra+".fastq") == True:
        print("RESTARTING " + sra + " .FASTQ DOWNLOAD")
        os.remove(sra+".fastq")
        subprocess.run(['fastq-dump',sra + ".sra"])
        os.remove(sra+".sra")
#Skipping the download if already downloaded
    elif os.path.isfile(sra+".fastq") == True and os.path.isfile(sra+".sra") == False:
        print(sra + " .FASTQ ALREADY DOWNLOADED")
        continue
      
    #subprocess.run(['fastq-dump',sra])
# open SRR_Acc_list.txt
# use pandas
# read.csv with pandas

# for every line
#   get the SRR number
#   download the SRA file


#Conda tips
#1) On osc enable python with ...
# module load python
# module load sratoolkit
#2) Create environment with
# conda create -n getsra
#3) Activate environment
# conda activate getsra
# source activate getsra
#4) Install pandas
# conda install pandas
#5) list environments on system

