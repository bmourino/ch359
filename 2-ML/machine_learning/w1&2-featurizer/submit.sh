#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name featurizing
#SBATCH --get-user-env
#SBATCH --ntasks    1
#SBATCH --cpus-per-task   48
#SBATCH --mem 32G
#SBATCH --time       24:00:00

module purge
python ofm_feature_generator.pyw