#!/bin/sh

#end to end from normal music to no_staff music
#remember you can get to MyBook thru ~/Volumes
on_ctrl_c(){
             echo "Ignoring Ctrl-C"
         }


echo -n "Enter name of file to process"
read im_raw 

echo -n "Enter name of output file"
read output

#convert normalize size
python2 scale_image.py $im_raw "a.png"

#clean with imagemajik
convert "a.png" -level 45% "b.png"

#staff removal
python2 gameraStaffRemoval.py "b.png" $output

#clean
rm a.png b.png

echo "complete"



