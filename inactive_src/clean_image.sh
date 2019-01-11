#!/bin/sh

#use imagemajick to clean inputed image file. 
#remember to run "chmod +x filename.sh"
#remember you can get to MyBook thru ~/Volumes
on_ctrl_c(){
             echo "Ignoring Ctrl-C"
         }

echo -n "Enter name of file to process"
read im_raw 

echo -n "Enter name of output file"
read output

convert $im_raw -level 45% $output

echo "complete"



