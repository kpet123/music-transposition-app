#gets connected compnents from sheet music file then pickles
# Import the Gamera core and initialize it
#PICKLE STRUCTURE
#[ {"arr"=_, "offset_x"=_, "offset_y=_},
#   ....
#   ...
# {"arr"=_, "offset_x"=_, "offset_y=_}  ]
#   

import sys
from gamera.core import *
init_gamera()
import cPickle


image = load_image(sys.argv[-1])
onebit = image.to_onebit()


component_list = onebit.cc_analysis()

print len(component_list)

system_list = []
for c in component_list:
    size = c.ncols*c.nrows 

    #find systems, rule out by length and size
    if size > onebit.ncols*20  and c.ncols > .6*onebit.ncols:
        arr = c.to_numpy()/c.label #1s and 0s, 1 is black
        print "coordinate of cc is "+str(c.offset_x)+","+str(c.offset_y)
        system_list.append({"arr": arr, "offset_x": c.offset_x, \
                "offset_y": c.offset_y})
with open("systems.pkl", "w") as f : 
        cPickle.dump(system_list, f, cPickle.HIGHEST_PROTOCOL)


