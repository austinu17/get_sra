Using get_sra.py followed by the SRR_Acc_List.txt file for the experiment, the sra file from NCBI will be and .fastq files will be downloaded from NCBI onto the local drive.

# Using get_sra to convert files

conda env create -f environment.yml -n Hello_World
conda activate Hello_World
python get_sra.py SRR_Acc_List.txt


Credit to Ohio State Data Science Club
