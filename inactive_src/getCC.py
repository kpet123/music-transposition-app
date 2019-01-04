#adapted from gamera_getCC.py
#gets connected compnents from sheet music file then pickles


import sys
import pickle
from skimage import measure
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import im_functions

img = mpimg.imread(sys.argv[1]) #must be png
img = im_functions.format_doc(img)


blob_img = measure.label(img) #arr with different values labeling each cc
component_list = measure.regionprops(blob_img) #list of ccs and their attributes
print( len(component_list))

system_list = [] #list with all systems

#generate system_list
for c in component_list:
   
    #find systems, rule out by size
	if c['bbox_area'] > len(img[0])* len(img)/100:
		bbox=c['bbox']
		#remove staff in system
		print("cc is ",  img[bbox[0]:bbox[2],bbox[1]:bbox[3]])
		c_staff, c_nostaff = im_functions.staff_separation(img[bbox[0]:bbox[2],\
							  bbox[1]:bbox[3]])

		#TEST
		plt.imsave("gen_ims/"+str(c)+"staff.png", c_staff)
		plt.imsave("gen_ims/"+str(c)+"nostaff.png", c_nostaff) 
		system_list.append({"no_staff_img" : c_nostaff,\
						    "just_staff_img" : c_staff,\
							"offset_x" : bbox[1], \
                			"offset_y" : bbox[0],\
							"all_features" : c})
 

with open("systems.pkl", "wb") as f : 
    pickle.dump(system_list, f, pickle.HIGHEST_PROTOCOL)
