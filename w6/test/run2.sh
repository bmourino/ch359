#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name="acs_calc"
#SBATCH --get-user-env
#SBATCH --output=_scheduler-stdout.txt
#SBATCH --error=_scheduler-stderr.txt
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=03:00:00


#SBATCH --mail-type=ALL
#SBATCH --mail-user=yi-yi.ly@epfl.ch

  source /ssoft/spack/bin/slmodules.sh -r deprecated
  module load intel
  module load intel-mpi intel-mkl
  module load cp2k/5.1-mpi


'srun' '-n' '1' '/ssoft/spack/cornalin/v2/opt/spack/linux-rhel7-x86_E5v4_Mellanox/intel-17.0.2/cp2k-5.1-gke4ujsx5qhx6zt7ncfo22hajqhp6n6b/bin/cp2k.popt' '-i' 'acs_mof.inp'  > 'acs_mof.out' 2>&1
