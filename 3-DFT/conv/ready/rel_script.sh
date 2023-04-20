#!/bin/bash
 
rel_cutoffs="10 20 30 40 50 60 70 80 90 100"
 
potential_file=GTH_POTENTIALS
template_file=template.inp
input_file=mof5.inp
coords_file= # complete
 
cutoff=250
 
for ii in $rel_cutoffs ; do
    work_dir=rel_cutoff_${ii}Ry
    if [ ! -d $work_dir ] ; then
        # complete to make directory
    else
        rm -r $work_dir/*
    fi
    sed -e "s/LT_cutoff/${cutoff}/g" \
        -e "s/LT_rel_cutoff/${ii}/g" \
        # complete to write input file from template, adding the current cutoff in the loop
    cp $coords_file $work_dir/
done
