#!/bin/bash -l
#SBATCH --no-requeue
#SBATCH --job-name="ta-mof-test"
#SBATCH --get-user-env
#SBATCH --output=_scheduler-stdout.txt
#SBATCH --error=_scheduler-stderr.txt
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=12
#SBATCH --time=06:00:00


#SBATCH --partition=normal
#SBATCH --account=pr128
#SBATCH --constraint=gpu
#SBATCH --mail-type=ALL
#SBATCH --mail-user=beatriz.buenomourino@epfl.ch

export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
source $MODULESHOME/init/bash
export CRAY_CUDA_MPS=1
ulimit -s unlimited
module load daint-gpu


###  code prepend_text start ###
module load CP2K/9.1-CrayGNU-21.09-cuda
###  code prepend_text end ###


'srun' '-n' '36' '/apps/dom/UES/jenkins/7.0.UP03/21.09/dom-gpu/software/CP2K/9.1-CrayGNU-21.09-cuda/bin/cp2k.psmp' '-i' 'UTSA_80_geopt.inp'  > 'UTSA80.out' 2>&1

 

False
