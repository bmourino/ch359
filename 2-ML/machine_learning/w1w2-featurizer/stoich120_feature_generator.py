# Here we use matminer to generate composition features as defined by Meredig et. al.
# Details of the API can be found here: https://hackingmaterials.lbl.gov/matminer/matminer.featurizers.composition.html#matminer.featurizers.composition.composite.Meredig
from matminer.featurizers.composition import Meredig
from ase.io import read
from pymatgen.io import ase as pm_ase
import numpy as np
import pandas as pd
import os
from tqdm import tqdm

# Settings
xyz_path = os.path.join('../../data','mofs.xyz') # list of appended XYZs (length N)
refcodes_path = os.path.join('../../data','refcodes.csv') # list of refcodes (length N)

#---------------------------------------
# Read in structures
ase_mofs = read(xyz_path, index=':')
refcodes = np.genfromtxt(refcodes_path, delimiter=',', dtype=str)
adaptor = pm_ase.AseAtomsAdaptor()
pm_mofs = #fillme (change the ase read object to pymatgen structures)
# Hint: to write for loop in one line with `My_list = [<expression> <for loop> <condition if any>]`

# Initialize feature object
featurizer = Meredig()
features = #fillme (generate feature names)
df = pd.DataFrame(columns=features)

# Get features
for i, pm_mof in enumerate(tqdm(pm_mofs)):
	fingerprint = featurizer.featurize(#fillme) (note: what is the input argument type the function required)
	refcode = refcodes[i]
	df.loc[refcode, :] = #fillme (store mof refcode and extracted features in pd.DataFrame)

# Export features
df.index.name = 'MOF'
df.to_csv('../../data/features/stoich120_fingerprints.csv', index=True)
