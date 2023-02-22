# Here we use matminer to featurize MOFs into orbital field matrixs. 
# Details of the API can be found here: https://hackingmaterials.lbl.gov/matminer/matminer.featurizers.structure.html#matminer.featurizers.structure.matrix.OrbitalFieldMatrix
from matminer.featurizers.structure import OrbitalFieldMatrix
from ase.io import read
from pymatgen.io import ase as pm_ase
import numpy as np
import pandas as pd
import os
from tqdm import tqdm

# Settings
xyz_path = os.path.join('../../data','mofs.xyz') # appended list of XYZs (length N)
refcodes_path = os.path.join('../../data','refcodes.csv') # refcode for each structure (length N)

#---------------------------------------
# Read in structures
ase_mofs = read(xyz_path, index=':')
refcodes = np.genfromtxt(refcodes_path, delimiter=',', dtype=str)
adaptor = pm_ase.AseAtomsAdaptor()
pm_mofs = #fillme (change the ase read object to pymatgen structures)

# Initialize feature object
featurizer = OrbitalFieldMatrix(period_tag=True)
features = #fillme (generate feature names)
df = pd.DataFrame(columns=features)

# Get features
for i, pm_mof in enumerate(tqdm(pm_mofs)):
	fingerprint = featurizer.featurize(#fillme) (note: what is the input argument type the function required)
	refcode = refcodes[i]
	df.loc[refcode, :] = #fillme (store mof refcode and extracted features in pd.DataFrame)

# Export features
df.index.name = 'MOF'
df.to_csv('../../data/features/ofm_fingerprints.csv', index=True)
