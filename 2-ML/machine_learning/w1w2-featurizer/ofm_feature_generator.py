# Here we use matminer to featurize MOFs into orbital field matrixs. 
# Details of the API can be found here: https://hackingmaterials.lbl.gov/matminer/matminer.featurizers.structure.html#matminer.featurizers.structure.matrix.OrbitalFieldMatrix

import os
import time
import click

from matminer.featurizers.structure import OrbitalFieldMatrix
from ase.io import read
from pymatgen.io import ase as pm_ase
import numpy as np
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool

# Settings
xyz_path = os.path.join('../../data','mofs.xyz') # appended list of XYZs (length N)
refcodes_path = os.path.join('../../data','refcodes.csv') # refcode for each structure (length N)

#---------------------------------------
# Read in structures
begin = 0
end = 20
ase_mofs = read(xyz_path, index=':')[begin:end]  # We only use the first 20 structures as a test
refcodes = np.genfromtxt(refcodes_path, delimiter=',', dtype=str)
adaptor = pm_ase.AseAtomsAdaptor()
pm_mofs = #fillme (change the ase read object to pymatgen structures)

# Initialize feature object
featurizer = OrbitalFieldMatrix(period_tag=True)
features = #fillme (generate feature names)
df = pd.DataFrame(columns=features)

# Note: the number defined here should not excess your CPU cores (8 in most cases)
number_of_cores = 6
print(f"The number of allocated cores is: {number_of_cores}")

# Get features
# Run the featurization in parallel
with Pool(number_of_cores) as mp_pool:
	results = tqdm(mp_pool.map(featurizer.featurize, pm_mofs), total=len(pm_mofs))
	for i, fingerprint in enumerate(results):
		df.loc[#fillme, :] = #fillme	# record the MOF name and its fingerprint

# Export features
df.index.name = 'MOF'
df.to_csv('../../data/features/ofm_fingerprints_%s_%s.csv' %(begin,end), index=True)
