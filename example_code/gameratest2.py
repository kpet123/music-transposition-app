from gamera.toolkits.skeleton import *
import sys
from gamera.core import *
init_gamera()


color = sys.argv[1]
direction = sys.argv[2]
img = load_image("process_img.png")
img = img.to_onebit()
proj_arr = img.run_histogram(color, direction)

with open("runs.dat", "w+") as runs:
    runs.write("set terminal png\n")
    runs.write("set xrange [0:30]    #optional for setting xrange\n")
    runs.write("plot '-' with impulses title 'black horizontal runs'\n")

    for counter, value in enumerate(proj_arr):
        runs.write(str(counter)+ " "+str(value)+"\n")
    runs.write("e\n")





