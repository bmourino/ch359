## Introduction
There are two python scripts featurize MOFs using composition method and orbital field matrix (OFM) method, respectively. 

## Run stoich120
* You need to fill the spaces in the python scripts. 

* And then run the python script in the conda environment that you have created for this project. 

## Run OFM on hpc
For OFM it will be a little bit tricky. It would take several days if we run it on local machines for our ~20,000 MOFs. Therefore, we need the high-performance cluster (hpc) here. 

* Log in your account on hpc by `ssh <username>@jed.epfl.ch`

* Follow the steps in the front page to clone the repository and install the conda environment and activate the environment

* Copy the files generated from previous steps (i.e. `mofs.xyz` and `refcodes.csv`) to cluster if needed using `scp <path-to-file> <target-path-on-hpc>`

* Make `submit.sh` an executable file using `chmod u+x submit.sh`

* After filling the space in `ofm_feature_generator.py`, submit the job by `sbatch submit.sh`. 

* You can check the status of your job by `squeue --user <username>`