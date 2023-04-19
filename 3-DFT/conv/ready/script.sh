#!/bin/bash
 
cutoffs="50 100 150 200 250 300 350 400 450 500 550 600 650 700"
 
template_file=template.inp
input_file=mof5.inp
coords_file= # complete
 
rel_cutoff=60 
 
for ii in $cutoffs ; do
    work_dir=cutoff_${ii}Ry
    if [ ! -d $work_dir ] ; then
        # complete to make directory
    else
        rm -r $work_dir/*
    fi
    sed -e "s/LT_rel_cutoff/${rel_cutoff}/g" \
        -e "s/LT_cutoff/${ii}/g" \
        # write input file from template, adding the current cutoff in the loop
    cp $coords_file $work_dir/
done
