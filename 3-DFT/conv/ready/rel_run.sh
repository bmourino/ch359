#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name=<your-job-name>
#SBATCH --get-user-env
#SBATCH --mem 30G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=36
#SBATCH --time=8:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user <your-email>
module load intel
module load gcc/11.3.0
module load openmpi/4.1.3
module load cp2k/9.1-mpi-openmp

rel_cutoffs="10 20 30 40 50 60 70 80 90 100"

input_file=mof5.inp
output_file=mof5.out

for ii in $rel_cutoffs ; do
    work_dir=rel_cutoff_${ii}Ry
    cd $work_dir
    if [ -f $output_file ] ; then
        rm $output_file
    fi
'srun' '-n' '36' '/ssoft/spack/syrah/v1/opt/spack/linux-rhel8-skylake_avx512/gcc-11.3.0/cp2k-9.1-klrakkis7sb24thlwnxd7slve3qwspxm/bin/cp2k.popt' '-i' 'mof5.inp'  > $output_file 2>&1
    cd ..
done
wait
