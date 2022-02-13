#!/bin/bash
#Usage # sbatch [this script]
#Name of the job
#SBATCH --job-name=10k-15kPau
#Runtime of the job - one day should be sufficient for datasets with up to 1000 genomes & 32 cores

#SBATCH --time=7-00:00:00
#Define sdout path
#SBATCH --output=/home/ruizro/prueba_script/reannot_and_mnv/10000-15000Paula.o
#Define sderr path
#SBATCH --error=/home/ruizro/prueba_script/reannot_and_mnv/10000-15000Paula.e
#Define the queue (Quality Of Service) to which the task shall be submitted to
#SBATCH --nodes=1
#SBATCH --partition=long
#SBATCH --mem=10000
#SBATCH --cpus-per-task=12

module load python/3.8
time python3 master_script.py -p /storage/PGO/data/mtb/mappings/v1/ -g gnum.3.paula.txt