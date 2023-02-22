# Here we use matminer to featurize MOFs into orbital field matrixs. 
# Details of the API can be found here: https://hackingmaterials.lbl.gov/matminer/matminer.featurizers.structure.html#matminer.featurizers.structure.matrix.OrbitalFieldMatrix
from matminer.featurizers.structure import OrbitalFieldMatrix
from ase.io import read
from pymatgen.io import ase as pm_ase
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
from multiprocessing import Pool

def run():
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
	
	# number of cores you have allocated for your slurm task
	number_of_cores = int(os.environ['SLURM_CPUS_PER_TASK'])

	# Get features
	with Pool(number_of_cores) as mp_pool:
		results = mp_pool.map(featurizer.featurize, tqdm(pm_mofs))
		for i, fingerprint in enumerate(results):
			df.loc[#fillme, :] = #fillme	# record the MOF name and its fingerprint

	# Export features
	df.index.name = 'MOF'
	df.to_csv('../../data/features/ofm_fingerprints.csv', index=True)

if __name__ == '__main__':
	run()
