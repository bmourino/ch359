# MOF Database & Machine Learning

In this part, we will learn how to build a quantitative structure property relation model for band gap of MOFs. MOFs are a class of materials that have a wide range of applications in various fields, including gas storage, catalysis, and drug delivery. The band gap of a MOF is a key property that determines its electronic and optical properties.

During the project, we will perform different approaches to featurize MOFs. Featurization is the process of transforming raw data (MOF structures) into numerical features that can be used as input to a machine learning model. We will learn different featurization techniques, including composition features and orbital field matrix features.

After featurizing the MOFs, we will train machine learning models to predict the band gap of MOFs. We will use kernel ridge regression (KRR) algorithm to build predictive models.

Once the models are trained, we will analyze the model performance and explain why the featurization approach is good or not for band gap prediction. Through this project, you will gain practical experience in using machine learning to solve real-world problems in materials science.

## How to run it
* Most of the scripts are in Python language. Every week, we need to fill the scripts in one subfolder of the `machine_learning` folder and finish one section of the jupyter notebook `utils/analysis.ipynb`. 

* All the data you will need are provided in the `data` folder. 

* Make sure you have activated the conda environment that you have installed for the project before you run any codes on any platform. 

# References
* A.S. Rosen, S.M. Iyer, D. Ray, Z. Yao, A. Aspuru-Guzik, L. Gagliardi, J.M. Notestein, R.Q. Snurr. "Machine Learning the Quantum-Chemical Properties of Metal–Organic Frameworks for Accelerated Materials Discovery", *Matter*, **4**, 1578-1597 (2021). DOI: [10.1016/j.matt.2021.02.015](https://doi.org/10.1016/j.matt.2021.02.015).
* A.S. Rosen, V. Fung, P. Huck, C.T. O'Donnell, M.K. Horton, D.G. Truhlar, K.A. Persson, J.M. Notestein, R.Q. Snurr. "High-Throughput Predictions of Metal–Organic Framework Electronic Properties: Theoretical Challenges, Graph Neural Networks, and Data Exploration," *npj Comput. Mat.,* **8**, 112 (2022). DOI: [10.1038/s41524-022-00796-6](https://doi.org/10.1038/s41524-022-00796-6).
