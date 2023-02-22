# CH-359 Projects in Computational Chemistry @ EPFL

Supporting scripts, tutorials and materials for CH-359 Projects in Computational Chemistry @ EPFL

## How to approach this repository

This is the private version, with all the answers and comments. #todo: create a public version

It is divided by 3 parts  and inside each folder there will be an explanation on how to install the required packages, scritps to run (tutorials and exercises) and a commented solution.

You might need to install minconda before, check [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).

Setup your environment with:

    $ git clone https://github.com/bmourino/ch359.git
    $ conda env create --file environment.yml
    $ conda activate ch359
    $ pip install umap pyeqeq oximachinerunner manage_crystal rdkit

Alternative (if taking too long):

    $ git clone https://github.com/bmourino/ch359.git
    $ conda install -c conda-forge mamba
    $ mamba env create --file environment.yml
    $ conda activate ch359
    $ pip install umap pyeqeq oximachinerunner manage_crystal rdkit


#todo: test environment setup

# Overview

## MOFs 101

- Metal  Organic  Frameworks  (MOFs)  are  porous,  crystalline  materials 
formed by metal nodes connected by organic linkers.[1](https://pubs.rsc.org/en/content/articlehtml/2020/ta/c9ta13506e#fn1)
Explored for optoelectronic properties in, e.g., photocatalysis.[1](https://pubs.rsc.org/en/content/articlehtml/2020/ta/c9ta13506e#fn1)
- Goal:  Computationally  handle  MOFs  -  visualize,  clean  and  get  an 
overview on basic properties.

## MOF Database & Machine Learning

![](./images/qmoflogo.png)

- Database on electronic properties of MOFs.[2](https://www.sciencedirect.com/science/article/pii/S2590238521000709)
- Goal: Quantitative structure property relationship modelling of MOF band 
gaps.
- How: Build ML models step by step, i.e., data preparation, model training, 
and  model  evaluation.  Compare  different  featurization  methods  and 
analyze their effects on models.

## MOFs & DFT: Digging deeper

![](./images/mof5.png)

- MOF-5: Explored extensively for its electronic properties.[3](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.1c00543)
- Goal: Take a deeper, critical look into DFT band gaps.
- How:  Find  ground  state  and  perform  calculations  with  different 
functionals. Compare with literature, and with values predicted from your 
ML model.

## Learning outcomes

- Understand  advantages  and  limitations  of  ML  and  DFT  to  obtain  band 
gaps.
- Understand the difference between fundamental and optical gaps.

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