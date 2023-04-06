#!/bin/bash

#SBATCH --no-requeue
#SBATCH --job-name  <your-job-name>
#SBATCH --get-user-env
#SBATCH --ntasks    1
#SBATCH --cpus-per-task 16
#SBATCH --mem   30G
#SBATCH --time 24:00:00

python <path_to_python_file>