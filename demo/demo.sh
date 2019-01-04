#!/bin/sh

#demo of what transposition app does thus far

on_ctrl_c(){
             echo "Ignoring Ctrl-C"
         }   
#prompt output filename
echo -n "Enter name of output file"
read outputfile

#clean image
chmod +x ../src/full_clean_image.sh
../src/full_clean_image.sh

#generate score

echo -n "At this point, this transposition app is able to move the staff up and down relative to the notes."

echo -n " Would you like to move the staff 'up' or 'down'?"
read direction

echo -n "What is the distance (in pitches) you would like to move the staff?"
read displacement


python ../src/generate_transposed_score.py output1.png  $displacement $direction $outputfile


#clean directory

rm output1.png

echo -n "Staff shifting complete. Look for generated file in demo directory"

