#imports
from __future__ import print_function 

import os
import re
import sys
import contextlib

import numpy as np
import pandas as pd # type: ignore
import seaborn as sns # type: ignore

import matplotlib.pyplot as plt # type: ignore
import matplotlib.style as style # type: ignore
from matplotlib.lines import Line2D # type: ignore
import matplotlib.transforms as mtransforms # type: ignore


# settings
style.use('seaborn-paper')
dirpath = os.getcwd()
sns.set_context('paper')


@contextlib.contextmanager
def smart_open(filename=None):
    if filename and filename != '-':
        fhandle = open(filename, 'w')
    else:
        fhandle = sys.stdout

    try:
        yield fhandle
    finally:
        if fhandle is not sys.stdout:
            fhandle.close()

def pdos_parser(pdosfilename,natoms,sigma=0.02,int_step_size=0.001,total_sum=False,no_header=False):
    """
    Convert the discrete CP2K PDOS points to a smoothed curve using convoluted gaussians.

    Also shifts the energies by the Fermi energy (so the Fermi energy will afterwards be at 0),
    and normalizes by the number of atoms of this kind.
    """

    # Copyright (c) 2017 Tiziano Müller <tiziano.mueller@chem.uzh.ch>,
    # based on a Fortran tool written by Marcella Iannuzzi <marcella.iannuzzi@chem.uzh.ch>
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program. If not, see <http://www.gnu.org/licenses/>.

    log = []
    HEADER_MATCH = re.compile(
    r'\# Projected DOS for atomic kind (?P<element>\w+) at iteration step i = \d+, E\(Fermi\) = [ \t]* (?P<Efermi>[^\t ]+) a\.u\.')

    with open(pdosfilename, 'r') as fhandle:
        header = HEADER_MATCH.match(fhandle.readline().rstrip())
        if not header:
            print(("The file '{}' does not look like a CP2K PDOS output.\n"
                   "If it is indeed a correct output file, please report an issue at\n"
                   "    https://github.com/dev-zero/cp2k-tools/issues").format(pdosfilename))
            log.append(("The file '{}' does not look like a CP2K PDOS output.\n"
                   "If it is indeed a correct output file, please report an issue at\n"
                   "    https://github.com/dev-zero/cp2k-tools/issues").format(pdosfilename))
            sys.exit(1)

        efermi = float(header.group('Efermi'))
        element = str(header.group('element'))
        # header is originally: ['#', 'MO', 'Eigenvalue', '[a.u.]', 'Occupation', 's', 'py', ...]
        header = fhandle.readline().rstrip().split()[1:]  # remove the comment directly
        header[1:3] = [' '.join(header[1:3])]  # rejoin "Eigenvalue" and its unit
        data = np.loadtxt(fhandle)  # load the rest directly with numpy

    npnts, ncols = data.shape
    ncols -= 3  # ignore energy, occupation and #MO for mesh

    emin = min(data[:, 1]) - 0.2 # energies are in the second column
    emax = max(data[:, 1]) + 0.2
    nmesh = int((emax-emin)/int_step_size)+1

    # printing to stderr makes it possible to simply redirect the stdout to a file
    print("# of lines:       {:14d}".format(npnts), file=sys.stderr)
    print("Integration step: {:14.3f}".format(int_step_size), file=sys.stderr)
    print("Sigma:            {:14.3f}".format(sigma), file=sys.stderr)
    print("Minimum energy:   {:14.3f}".format(emin), file=sys.stderr)
    print("Maximum energy:   {:14.3f}".format(emax), file=sys.stderr)
    print("# of mesh points: {:14d}".format(nmesh), file=sys.stderr)

    log.append("# of lines:       {:14d}".format(npnts))
    log.append("Integration step: {:14.3f}".format(int_step_size))
    log.append("Sigma:            {:14.3f}".format(sigma))
    log.append("Minimum energy:   {:14.3f}".format(emin))
    log.append("Maximum energy:   {:14.3f}".format(emax))
    log.append("# of mesh points: {:14d}".format(nmesh))

    # reproduce exactly the previous Fortran-based code
    xmesh = np.array([emin+i*int_step_size for i in range(1, nmesh+1)])
    ymesh = np.zeros((nmesh, ncols))

    fact = int_step_size/(sigma*np.sqrt(2.0*np.pi))
    for mpnt in range(nmesh):
        func = np.exp(-(xmesh[mpnt]-data[:, 1])**2/(2.0*sigma**2))*fact
        ymesh[mpnt, :] = func.dot(data[:, 3:])

    if total_sum:
        finalsum = np.sum(ymesh, 0)*int_step_size
        print("Sum over all meshpoints, per orbital:", file=sys.stderr)
        print(("{:16.8f}"*ncols).format(*finalsum), file=sys.stderr)
        log.append("Sum over all meshpoints, per orbital:")
        log.append(("{:16.8f}"*ncols).format(*finalsum))

    xmesh -= efermi  # put the Fermi energy at 0
    xmesh *= 27.211384  # convert to eV
    ymesh /= natoms  # normalize

    output = pdosfilename.split('aiida-')[0] + (pdosfilename.split('aiida-')[-1]).split('k')[0] + element + '.dat'

    with smart_open(output) as fhandle:
        if not no_header:
            print(("{:>16}" + " {:>16}"*ncols).format("Energy_[eV]", *header[3:]), file=fhandle)
        for mpnt in range(nmesh):
            print(("{:16.8f}" + " {:16.8f}"*ncols).format(xmesh[mpnt], *ymesh[mpnt, :]), file=fhandle)
    
    return output,log


def get_pdosdat_paths(pdospathpbe,natoms,pdospathpbe0=None):
        pdosfiles = {'pbe':[]}
        log = {'pbe':[]}
        for i in os.listdir(pdospathpbe):
            if i.endswith('pdos'):
                filename = pdospathpbe + '/' + i
                temp = pdos_parser(filename,natoms,sigma=0.001,int_step_size=0.001,total_sum=True) 
                pdosfiles['pbe'].append(temp[0])
                log['pbe'].append(temp[1])
        if pdospathpbe0:
            pdosfiles['pbe0'] = []
            log['pbe0'] = []
            for i in os.listdir(pdospathpbe0):
                if i.endswith('pdos'):
                    filename = pdospathpbe0 + '/' + i
                    temp = pdos_parser(filename,natoms,sigma=0.001,int_step_size=0.001,total_sum=True) 
                    pdosfiles['pbe0'].append(temp[0])
                    log['pbe0'].append(temp[1])

        return pdosfiles


## parameters for plotting
def set_size(width, fraction=1):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float
            Document textwidth or columnwidth in pts
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure (in pts)
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

fig_sizes = set_size(252.945)
fig_sizes2 = set_size(505.89)
plt.rcParams['lines.markersize'] = 2.5
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"

def plot_pdos(pdosfiles,label,outputpath):
    # not working for different spins (has to be closed shell), but working for pbe vs pbe0

    fig_sizes = set_size(252.945)

    THIS_DIR = os.path.dirname(os.path.realpath(__file__))
    colors = pd.read_csv(THIS_DIR + '/colors.csv')

    if 'pbe0' in pdosfiles.keys():
        r, axs = plt.subplot_mosaic([['a'],['b']],figsize=fig_sizes,sharey=True,sharex=True)
    else:
        r, axs = plt.subplot_mosaic([['a']],figsize=fig_sizes)

    for l, ax in axs.items():
        # label physical distance to the left and up:
        trans = mtransforms.ScaledTranslation(-20/72, 7/72, r.dpi_scale_trans)
        ax.text(0.15, 1.0, l, transform=ax.transAxes + trans,
                fontsize=8, weight='bold')

    legend_elements = []
    for i in pdosfiles['pbe']:
        data = np.loadtxt(fname=i,skiprows=1)
        # spin = ((i.split('-')[-1]).split('.')[0]).split('_')[0]
        atom = ((i.split('/')[-1]).split('.')[0])
        if atom != 'H':
            color = '#' + colors.loc[colors.Element==atom]['Hex'].item()
            X=data[:,0]
            Yini=np.delete(data,0,axis=1)
            Y=np.sum(Yini,axis=1)
            axs['a'].fill_between(X, Y, 0, facecolor=color, alpha=0.5)
            axs['a'].plot(X, Y, linewidth= 0.5 , color=color, label=atom)
            # axs['a'].set_title('PBE, spin up', fontsize=8)
            legend_elements.append(Line2D([0], [0], marker='.', color=color, label=atom))

    if 'pbe0' in pdosfiles.keys():
        for i in pdosfiles['pbe0']:
            data = np.loadtxt(fname=i,skiprows=1)
            # spin = ((i.split('-')[-1]).split('.')[0]).split('_')[0]
            atom = ((i.split('/')[-1]).split('.')[0])
            if atom != 'H':
                color = '#' + colors.loc[colors.Element==atom]['Hex'].item()
                X=data[:,0]
                Yini=np.delete(data,0,axis=1)
                Y=np.sum(Yini,axis=1)
                axs['b'].fill_between(X, Y, 0, facecolor=color, alpha=0.5)
                axs['b'].plot(X, Y, linewidth= 0.5 , color=color, label=atom)
                # axs['b'].set_title('PBE0, spin up', fontsize=8)

    ###
    # r.suptitle(label, fontsize=8)
    r.legend(handles=legend_elements, loc='upper center', markerscale=1, ncol=len(legend_elements), fontsize=6, frameon=False)

    for i in axs.keys():
        axs[i].tick_params(labelsize=8)
        axs[i].set_xlim(-1.2, 6)
        axs[i].set_ylim(0, 0.0055)
        axs[i].set_yticklabels([])

    r.text(0.5, 0, 'PDOS [a.u]', ha='center', va='center', fontsize=8)
    r.text(0, 0.5, r'Energy$-E_F$ [eV]', ha='center', va='center', rotation='vertical', fontsize=8)
    
    label_fig = label + "_DOS.pdf"
    output = os.path.abspath(os.path.join(outputpath, label_fig))
    r.tight_layout()
    r.savefig(output, bbox_inches='tight')