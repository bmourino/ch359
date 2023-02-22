from ase.io import read, write
import os
from tqdm import tqdm

cif_path = r'../data/cifs'
cifs = os.listdir(cif_path)
cifs.sort()

refcodes = []
mofs = []
for cif in tqdm(cifs):
	refcodes.append(cif.split('.cif')[0])
	mofs.append(read(os.path.join(cif_path, cif)))
write('../data/mofs.xyz', mofs)

with open('../data/refcodes.csv','w') as w:
	for refcode in refcodes:
		if refcode == refcodes[-1]:
			w.write(refcode)
		else:
			w.write(refcode+',')
