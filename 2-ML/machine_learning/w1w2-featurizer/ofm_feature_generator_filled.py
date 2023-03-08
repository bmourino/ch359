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

@click.command('cli')
@click.argument('begin', type=int)
@click.argument('end', type=int)
def run(begin, end):
	# Settings
	xyz_path = os.path.join('../../data','mofs.xyz') # appended list of XYZs (length N)
	refcodes_path = os.path.join('../../data','refcodes.csv') # refcode for each structure (length N)

	#---------------------------------------
	# Read in structures
	ase_mofs = read(xyz_path, index=':')
	refcodes = np.genfromtxt(refcodes_path, delimiter=',', dtype=str)
	adaptor = pm_ase.AseAtomsAdaptor()
	pm_mofs = [adaptor.get_structure(ase_mof) for ase_mof in ase_mofs[begin:end]]

	# Initialize feature object
	featurizer = OrbitalFieldMatrix(period_tag=True)
	features = featurizer.feature_labels()
	df = pd.DataFrame(columns=features)

	# Define the number of cores
	number_of_cores = 6
	print(f"The number of allocated cores is: {number_of_cores}")

	# Get features
	with Pool(number_of_cores) as mp_pool:
		results = tqdm(mp_pool.map(featurizer.featurize, pm_mofs), total=len(pm_mofs))
		for i, fingerprint in enumerate(results):
			df.loc[refcodes[begin+i], :] = fingerprint

	# Export features
	df.index.name = 'MOF'
	df.to_csv('../../data/features/ofm_fingerprints_%s_%s.csv' %(begin,end), index=True)

if __name__ == '__main__':
	run()