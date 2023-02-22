# ml_CompuationalChemistry

In this project, we will learn how to use machine learning to predict the band gaps of Metal-Organic Frameworks (MOFs). MOFs are a class of materials that have a wide range of applications in various fields, including gas storage, catalysis, and drug delivery. The band gap of a MOF is a key property that determines its electronic and optical properties.

During the project, we will perform different approaches to featurize MOFs. Featurization is the process of transforming raw data (MOF structures) into numerical features that can be used as input to a machine learning model. We will learn different featurization techniques, including composition features, orbital field matrix features, and the smooth overlap of atomic positions (SOAP) features.

After featurizing the MOFs, we will train machine learning models to predict the band gap of MOFs. We will use kernel ridge regression (KRR) algorithm to build predictive models.

Once the models are trained, we will analyze the model performance and explain why the featurization approach is good or not for band gap prediction. Through this project, you will gain practical experience in using machine learning to solve real-world problems in materials science.

## How to run it
This is a python program. In each file, we have left some space for you to help you understand the function of the file. 

## Run it locally
The following steps assume that you use MacOS or some Linux flavor. If you use Windows, we recommend that you first install the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).

* Create a new folder and clone this repository (you need `git` for this, if you get a `missing command` error for `git` you can install it with `sudo apt-get install git`).
```
git clone https://github.com/XiaoqZhang/ml_CompuationalChemistry.git
cd ml_ComputationalChemistry
```

* We recommend that you create a virtual conda environment on your computer in which you install the dependencies for this project. To do so head over to [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions there.

* Then, to create a conda environment named `ml_cc`, use
```
conda env create -f environment.yml -n ml_cc
```

* You can activate this environment using
```
conda activate ml_molsim
```

* After the environment is activated, to install all the python packages we need in this project, use
```
pip install -r requirement.txt
```

## Make modifications and get update

* Before you make any changes to the program, we suggest you create a new branch for your changes by 
```
git checkout -b <my-branch-name>
```

* After you made the changes, you can push it to your github fork by 
```
git push <remote-url-name> <my-branch-name>
```

* Every week, we will update the part of the program that we need for that week on github. 



# References
* A.S. Rosen, S.M. Iyer, D. Ray, Z. Yao, A. Aspuru-Guzik, L. Gagliardi, J.M. Notestein, R.Q. Snurr. "Machine Learning the Quantum-Chemical Properties of Metal–Organic Frameworks for Accelerated Materials Discovery", *Matter*, **4**, 1578-1597 (2021). DOI: [10.1016/j.matt.2021.02.015](https://doi.org/10.1016/j.matt.2021.02.015).
* A.S. Rosen, V. Fung, P. Huck, C.T. O'Donnell, M.K. Horton, D.G. Truhlar, K.A. Persson, J.M. Notestein, R.Q. Snurr. "High-Throughput Predictions of Metal–Organic Framework Electronic Properties: Theoretical Challenges, Graph Neural Networks, and Data Exploration," *npj Comput. Mat.,* **8**, 112 (2022). DOI: [10.1038/s41524-022-00796-6](https://doi.org/10.1038/s41524-022-00796-6).
