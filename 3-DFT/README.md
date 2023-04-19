# MOFs & DFT: Digging deeper

![](./../images/mof5.png)

- MOF-5 (CSD ID: MIBQAR, QMOF ID: qmof-a2d95c3): Explored extensively for its electronic properties.<sup>[3](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.1c00543)</sup>
- Goal: Take a deeper, critical look into DFT band gaps.
- How:  Find  ground  state  and  perform  calculations  with  different 
functionals. Compare with literature, and with values predicted from your 
ML model.

## DFT calculations & software

[CP2K](https://doi.org/10.1063/5.0007045) is an open source software package that can perform electronic structure calculations of many systems, and performs well for systems of large size such as many MOFs. In CP2K, this is possible due to the exploitation of parallel scalability and efficient algorithms.

Different than most packages, the electronic structure module QUICKSTEP in CP2K uses as basis set a combination of a Gaussian orbital scheme (Gaussian basis set to expand orbital functions) with plane wave auxiliary basis set. This is referred to as the Gaussian-Plane Waves (GPW) method.

You can find tutorials [here](https://www.cp2k.org/howto) and input reference manual [here](https://manual.cp2k.org/#gsc.tab=0) (you can always refer to this when writing the input).

We will use PBE (a GGA exchange-correlation functional) throughout sections 1 and 2. For section 3 we will vary functionals. Restart wavefunctions are provided for each calculation in sections 2 and 3 (use them to save computational resources!) and you should always double check with the TAs before submitting your calculation.


## Using SCITAS cluster

To make your life easier, you might want to configure a [passwordless SSH](https://www.redhat.com/sysadmin/passwordless-ssh).

All DFT calculations will be performed on the EPFL SCITAS cluster (in your case, helvetios). You can copy folders with `scp -r path/to/folder username@clusteraddress:destination/path` or analogously you can copy files (without `-r`).

### FINDING/LOADING MODULES

It could be useful to learn to locate an executable on the cluster. It's is necessary to submit calculations, and it will be different for different clusters. You can find the cp2k module with `module spider cp2k` and follow the instructions to see which modules you need to load (e.g. you can run `module spider cp2k/9.1-mpi-openmp`). Then, after loading the modules, you can do `module avail` and check the path for the cp2k folder. Join what appears on top, between `------`, and the desired cp2k folder (e.g. `cp2k/9.1-mpi-openmp`).  Check if you have the right path with `ls`. If this folder does not contain a `/bin/cp2k.popt` file, you might need to visualize the file you find (e.g. `cp2k/9.1-mpi-openmp.lua`) with `vi` and copy the path for the executable there. 

### SUBMITTING JOBS

To submit jobs, you should submit with `sbatch submission.sh` where `submission.sh` is your bash script containing information such as number of nodes, memory allocation, your email for logs, and the command to run the cp2k input file with the cp2k executable.

### HANDLING JOBS

With `squeue -all -u username` you can check what is on your queue, the job-id and if it is running or queued. With `scancel job-id` you can cancel the job if needed.


## Approaching this part

- Carefully check each file for modifications you should make
    - If it is a script, always try to understand what it is doing step by step
    - In input files, try to understand what each section you are modifying will control, and justify your choices for parameters

- Copy necessary folders to SCITAS cluster
- Follow steps for each section
- You can analyse your results in the respective jupyter notebooks in each section

## 0. Writing an input

To perform DFT calculations you will need to define in your input file:

- Your periodic MOF (can be directly parsed in the input file, or you can reference to an .xyz or .cif file
    
    *We already provide an .xyz file for MOF-5, but following the steps in 1-MOF901 you should be able to do it yourself*

- Your cell parameters

- The exchange-correlation functional of choice

- The basis set to be used (check [here](https://www.cp2k.org/basis_sets) for more information and [here](https://cp2k-basis.pierrebeaujean.net/) for possibilities)

- The pseudopotential (alternatively check [here](https://htmlpreview.github.io/?https://github.com/cp2k/cp2k-data/blob/master/potentials/Goedecker/index.html) for possibilities)

- Converged parameters that guarantee a fine enough integration grid

You will need to know the following about your MOF:

- Is it charged?

- Is it closed or open shell? What is the multiplicity? (if closed set UKS to False, if open set UKS to True)

- If open shell, what is the guess spin configuration?

You will find in `conv/ready/template.inp` the template for the input to be used when testing for convergence. Go through the file and make the modifications accordingly. For the multigrid section, it might be useful to read section **1. Looking for convergence**.

A good exercise would be to go through each section in the input and see if you can understand what it is doing.

| Section  | What it does  | Specifics     | 
| :---     | :---          | :---          |   
| GLOBAL   | Controls the run type (if it's single point, geometry optimization etc.) and print level (how much information we want)     | Usually print level medium gives us enough information, such as HOMO-LUMO gap      |  
| ... | ... | ... |

For reference on how to build an input for cp2k, check the [howto](https://www.cp2k.org/howto:static_calculation) on calculating energy and forces (static/single point calculation).

*Q$*: Why do we need to specify a pseudopotential?

*Q$*: Are we considering dispersion correction?

## 1. Looking for convergence

Usually, *ab initio* DFT makes use of real-space integration grid to represent, for example, the product of Gaussian functions. QUICKSTEP uses a multi-grip system that maps the latter onto real-space grids. This is an important step that makes sure that narrow/sharp Gaussians are treated differently than wide/smooth ones, i.e., the first will be mapped onto a finer grid and the latter, onto a coarser grid. 

It is crucial to make sure you are choosing a fine enough integration grid so as to obtain results that will not be largely limited in accuracy by the integration grid, instead it will be limited by other factors such as the functional of choice.

Here you will test for some parameters in the [MULTIGRID](https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/DFT/MGRID.html) section to be used in the following calculations, so you can choose the ones that will provide a fine enough integration grid. In the end, you should reach a compromise between computational cost and accuracy. You can check this by analysing how the total energy will vary (and how much more accurate it will become) as you choose more robust values for the parameters. Ideally we should test for the convergence everytime we are computing a different property.

The parameters to test are:

- [CUTOFF](https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/DFT/MGRID.html#list_CUTOFF) - planewave cutoff (default unit is in Ry) for the finest level of the multi-grid
- [REL_CUTOFF](https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/DFT/MGRID.html#list_REL_CUTOFF) - planewave cutoff of a reference grid covered by a Gaussian with unit standard deviation $e^{\vert\vec{r}\vert^2}$

For more information check the [howto](https://www.cp2k.org/howto:converging_cutoff) on converging cutoff.

*Q$*: What do you think happens to the grids if the CUTOFF is too low? And what happens if you have a high CUTOFF, but a REL_CUTOFF that is too low?



## 2. Structure relaxation

Using PBE, the error w.r.t. experimental structure is expected to be < 5%. 

For reference, check the [howto](https://www.cp2k.org/howto:geometry_optimisation) on geometry optimization

- Perform a single point calculation with the chosen CUTOFF and REL_CUTOFF (Ideally you should print cube and pdos files to compare with the results after relaxation)

- Perform geometry optimization

- Perform cell optimization (Print cube and pdos files in the last step to compare with results from single point calculation before relaxation)

*Q$*: Check how cell parameters vary, and how cube files change.
*Q$*: What is the difference between cell and geometry optimization? What is being optimized?
*Q$*: Is there any difference between LBFGS and BFGS optimization?


## 3. Testing different flavors

- Hybrid functionals

What hybrid functionals try to do is correct the deviation from piecewise linearity observed in Kohn-Sham DFT. It does that by adding a portion of Hartree-Fock exact exchange, either empirically, by a fixed amount, or non-empirically (for example, state of the art optimally-tuned screened range separated hybrid functionals - OT-SRSH).

*Q$*: Why do we need AUX_FIT basis for hybrid functionals?

*Q$*: What is the difference between HSE06 and PBE0? What is the fraction of Hartree-Fock exchange we use for each?

- Meta-GGA

SCAN (strongly-constrained and appropriately-normed) is a meta-GGA functional that adds the orbital kinetic energy density of each spin, for more information check [here](https://arxiv.org/abs/1511.01089) and [here](https://templeefrc.org/scan-overview).

*Q$*: When is SCAN a much better choice than PBE?

*Q$*: What can you say about the computational cost when you compare the hybrids with SCAN?

- TD-DFT

With DFT, any time you compute band gap your point of comparison is always the fundamental gap (difference between ionization potential and electron affinity). This is not easy to measure experimentally - you need photoemission and inverse photoemission spectroscopy. With time-dependent DFT, however, you can compute optical gap, that you can measure much more easily with UV-Vis spectroscopy and, e.g., Tauc plot fitting.


## 4. Analysing results

Plot density of states and compare band gaps for each functional and for TDDFT.

Compare structure parameters before and after relaxation.

Compare the band gaps with literature and your predicted band gap with machine learning.
