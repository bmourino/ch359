# How is my MOF doing?

This week we will learn how to perform sanity checks on MOFs, and investigate some basic properties such as geometric features and oxidation state.

Keep track of your answers to the questions that are marked with a *Q$*, it can be useful for the report!

## 1. Visualizing structures on Avogadro

### Installing Avogadro

Go to the [download](https://avogadro.cc) page on the website, and proceed with installation

*N.B.: Be patient, Avogadro unfortunately crashes sometimes. You can also try [GDIS](http://gdis.seul.org/), but you might run into issues to install it.*

### Tutorial - choose your structure and visualize!

1. Go to https://www.ccdc.cam.ac.uk/structures/ 
2. Search for a structure that you would like to visualize now – you choose!
3. On the tab “Results”, select the identifier of the structure (if not already selected) and choose Download – Download current entry; fill in with your information and download .cif
4. Open Avogadro
5. Can you tell what is the structure made of? 
6. What are the cell parameters (angles, vectors, total number of atoms in the unit cell, number of nonequivalent atoms)?
7. What is the symmetry of the cell?
8. What is the volume of the unit cell?

*hint: you can find information in View – Properties* 

9. Select Crystallography – Wrap Atoms to Cell
10. To fill the unit cell, go to Crystallography – Space group – Fill Unit Cell
9 and 10 are important for cases where the unit cell is not well defined 
11. In View – Crystal View Options – Repeat, change the values of A, B and/or C; set back to A=B=C=1 after
12. Build a supercell in Build – Super Cell Builder
13. What is the difference between repeating the cell and building a supercell?
14. Can you find a way to translate atom positions inside the unit cell?
15. What else can you think of doing with your structure?

*hint: you can find interesting tools in the Crystallography and Extensions section (keep in mind that it’s possible that some of them might crash); example: you might want to try changing the volume of the unit cell – what happens if you do it?*

Explorer mode: If you feel adventurous and up for a (laborious) challenge after class, you can try selecting a paper that has the crystallographic information of the structure and see if you can create a cif file yourself!

### Cleaning on Avogadro

Removing unwanted atoms:

1. Go to Select – Select by element to see which element it is according to color
2. Select this tool ![](./images/select_tool.png)
3. Pressing ctrl (or command on macos) select all atoms you wish to delete and remove it with backspace

*To think over: what do we mean by a “clean structure” and why do we need to make sure the structure is properly cleaned?*

## 2. Gathering information about our MOFs

Run the jupyter notebook with the following:

    $ jupyter notebook
    $ run-checks.ipynb

*Important: Make sure you are using the kernel ch359!*

Alternatively, you can try using [VSCode](https://code.visualstudio.com/).

*tips: “esc+b” will create a new block of code; “esc+dd” will delete the block of code you’re at; enter will add a new line in the same block of code; shift+enter will run the block of code.*

## 3. Managing structure files

You can convert between cif and xyz files (try to think: what is the difference between them?) with manage_crystal:

From .cif to .xyz:

    $ manage_crystal file.cif -o xyz

From .xyz to .cif:

1. Open the .xyz file with any text editor and on the second line add:

	CELL: A B C alpha beta gamma

*replace A with the value of A and so on*

2. Save new file (e.g.: file.xyz)

Converting to .cif:

    $ manage_crystal file.xyz -o cif


## 4. Other tools

Have a look at [MOFid/MOFkey](https://snurr-group.github.io/web-mofid/sbu.html) and [topcryst](https://topcryst.com/).

MOFid promotes a standardized approach to the naming of MOFs, you can read more about it [here](https://pubs.acs.org/doi/full/10.1021/acs.cgd.9b01050).

topcryst is a tool that allows you to evaluate the topology of a MOF, you can read more about it [here](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2088041).