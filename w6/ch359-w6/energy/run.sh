#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name=“project”
#SBATCH --mem 160000
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=12
#SBATCH --time=4:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user #<yourusername>@epfl.ch
source /ssoft/spack/bin/slmodules.sh -r deprecated #needed after summer 2018 (to check!)
module load intel
module load intel-mpi intel-mkl
module load cp2k/5.1-mpi

srun -n 180 /ssoft/spack/cornalin/v2/opt/spack/linux-rhel7-x86_E5v4_Mellanox/intel-17.0.2/cp2k-5.1-gke4ujsx5qhx6zt7ncfo22hajqhp6n6b/bin/cp2k.popt <your_input_file> > <your_output_file>
