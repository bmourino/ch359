import glob
import numpy as np
from matplotlib import rcParams

import matplotlib.pyplot as plt
import matplotlib.style as style 
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnchoredText
import seaborn as sns
import os

style.use('seaborn-paper')
dirpath = os.getcwd()
sns.set_context('paper')


plt.rc('font', family='Helvetica')
rcParams["legend.labelspacing"] = 0.4
rcParams["legend.columnspacing"] = 1
rcParams["legend.borderaxespad"] = 0.4
rcParams["legend.handletextpad"] = 0.5
rcParams["legend.markerscale"] = 1.5
rcParams["legend.fancybox"] = False
rcParams["legend.frameon"] = False

r, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True , figsize=(6,6))


##


data = np.loadtxt(fname="PDOS_C.dat",skiprows=1)
X=data[:,0]
Yini=np.delete(data,0,axis=1)
Y=np.sum(Yini,axis=1)
ax2.fill_between(X, Y, 0, facecolor='gray' , alpha =0.6)
ax2.plot(X, Y, linewidth = 0.5 , color ='black', label="C")

data = np.loadtxt(fname="PDOS_O.dat",skiprows=1)
X=data[:,0]
Yini=np.delete(data,0,axis=1)
Y=np.sum(Yini,axis=1)
ax2.fill_between(X, Y, 0, facecolor='red', alpha=0.6)
ax2.plot(X, Y, linewidth = 0.5 , color ='darkred', label="O")

data = np.loadtxt(fname="PDOS_B.dat",skiprows=1)
X=data[:,0]
Yini=np.delete(data,0,axis=1)
Y=np.sum(Yini,axis=1)
ax2.fill_between(X, Y, 0, facecolor='green', alpha=0.6)
ax2.plot(X, Y, linewidth = 0.5 , color ='darkgreen', label="B")


##


data = np.loadtxt(fname="PDOS_C0.dat",skiprows=1)
X=data[:,0]
Yini=np.delete(data,0,axis=1)
Y=np.sum(Yini,axis=1)
ax1.fill_between(X, Y, 0, facecolor='gray' , alpha =0.6)
ax1.plot(X, Y, linewidth = 0.5 , color ='black', label="C")

data = np.loadtxt(fname="PDOS_O0.dat",skiprows=1)
X=data[:,0]
Yini=np.delete(data,0,axis=1)
Y=np.sum(Yini,axis=1)
ax1.fill_between(X, Y, 0, facecolor='red', alpha=0.6)
ax1.plot(X, Y, linewidth = 0.5 , color ='darkred', label="O")

data = np.loadtxt(fname="PDOS_B0.dat",skiprows=1)
X=data[:,0]
Yini=np.delete(data,0,axis=1)
Y=np.sum(Yini,axis=1)
ax1.fill_between(X, Y, 0, facecolor='green', alpha=0.6)
ax1.plot(X, Y, linewidth = 0.5 , color ='darkgreen', label="B")


###
#ax1.annotate('PBE0', xy=(0.5, 0.5), textcoords='data', size=12, horizontalalignment='right', verticalalignment='top')
plt.suptitle('COF-5', fontsize=16, y=0.95)
at1 = AnchoredText("PBE0", prop=dict(size=12), frameon=True, loc='upper right')
at1.patch.set_boxstyle("square, pad=0.")
ax1.add_artist(at1)
at2 = AnchoredText("PBE", prop=dict(size=12), frameon=True, loc='upper right')
at2.patch.set_boxstyle("square, pad=0.")
ax2.add_artist(at2)


legend_elements = [Line2D([0], [0], color='dimgrey', lw=3, label='C'), Line2D([0], [0], color='red', lw=3, label='O'), Line2D([0], [0], color='darkgreen', lw=3, label='B')]
ax1.legend(handles=legend_elements, loc='upper left', fontsize=12, framealpha=1, frameon=True)
plt.setp( [a.get_xticklabels() for a in r.axes[:-1]], visible=False)
plt.setp( ax1, yticks=[])

plt.xticks(fontsize=14)
ax1.set_ylabel('PDOS [a.u]', fontsize=16)
ax2.set_ylabel('PDOS [a.u]',fontsize=16)

plt.xlim(-1.2, 5)
plt.ylim(0, 0.0055)
plt.xlabel(r'Energy$-E_F$ [eV]' , fontsize = 16)
#plt.rcParams["figure.figsize"] = (10,25)
plt.savefig("cof1-dos.png", dpi=300)

