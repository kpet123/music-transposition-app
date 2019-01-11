#!/bin/sh

#end to end from normal music to no_staff music
#remember you can get to MyBook thru ~/Volumes
on_ctrl_c(){
             echo "Ignoring Ctrl-C"
         }


echo -n "Enter name of file to process"
read im_raw 

#echo -n "Enter name of output file"
#read output

#convert normalize size
#python ../src/scale_image.py $im_raw a.png

#clean with imagemajik

magick convert $im_raw -colorspace Gray  -level 45% -auto-threshold OTSU "output1.png"

#clean
#rm a.png 

echo "Image cleaning complete"



