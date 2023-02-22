# CH-359 Projects in Computational Chemistry @ EPFL

Supporting scripts, tutorials and materials for CH-359 Projects in Computational Chemistry @ EPFL

# How to approach this repository

This is the private version, with all the answers and comments. #todo: create a public version

It is divided by 3 parts  and inside each folder there will be an explanation on how to install the required packages, scritps to run (tutorials and exercises) and a commented solution.

You might need to install minconda before, check [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).

Setup your environment with:

    $ git clone -b 2023-1 https://github.com/bmourino/ch359.git
    $ conda install -c conda-forge mamba
    $ mamba env create --file environment.yml
    $ conda activate ch359
    $ pip install umap pyeqeq oximachinerunner manage_crystal


#todo: test environment setup

# Plan 2023-1

| Date  | Week  | Topic                    | Specifics     | Ideas          |
| :---  | :---  | :---                     | :---          | :---           |   
| 23.02  | 1     | Introduction             | Project presentation and computational carpentry         |           |     
| 01.03  | 2     | (P1) How is my MOF doing?     | Get familiar with mofchecker, oximachine, manage_crystal, visualization, geometric features    | For cleaning, as exercise: PCN-223 - pial occupations; manually create lone molecules               |
| 08.03  | 3     | (P2) ML1             |         |           |    
| 15.03  | 4     | (P2) ML2             |         |           |    
| 22.03  | 5     | (P2) ML3             |         |           |    
| 29.03  | 6     | (P2) ML4             |         |           |    
| 05.04  | 7     | (P2) ML5             |         |           |    
| 12.04  | 8     | (P3) Looking for convergence  | Write inputs, perform sp with different cutoff, rel_cutoff, with and without supercell      | Use MOF-5               |
| 19.04  | 9	 | (P3) Looking for ground state | Write inputs, perform geo_opt and cell_opt and work on what's left from 1 |	|
| 26.04  | 10 	 | (P3) Testing different flavors| Write inputs for different functionals: PBE0, DFT+U, SCAN, xTB?	| **test before if it works! |
| 03.05  | 11    | (P3) Analyzing results	       | Plot density of states, analyze orbitals, and start with presentation	| Talk about fundamental vs optical gap; give them data on GW, BSE, TDDFT, experimental optical gap |
| 11.05  | 12    | Working on report and presentation	       |  |  |
| 18.05  | 13    | Public holiday	       |  |  |
| 25.05  | 14    | Mock presentation	       |  |  |
| 01.06  | 15    | Presentation	       |  |  |