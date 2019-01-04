# replaces areas deleted in staff removal


THICKNESS = 1

import numpy as np
import pickle
import im_functions
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage

with open("systems.pkl", "rb") as f:
	system_list = pickle.load(f)

#variables
system = system_list[0]
raw_staffs = system['just_staff_img']
raw_staff_copy = np.copy(raw_staffs)
spots_to_repair = raw_staffs
staff_width = len(raw_staffs[0])
THICKNESS = int(THICKNESS)

staff_locations, distance = im_functions.get_system_staff_location(raw_staffs)


blockspace = np.zeros((THICKNESS, staff_width))
for location in staff_locations:
	raw_staffs[location:location+THICKNESS, 0:staff_width] = blockspace

no_staff = system['no_staff_img']
repaired_image = no_staff+raw_staffs


#generate clean staff image
clean_staff = raw_staff_copy - spots_to_repair
structure = np.ones((THICKNESS, int(staff_width/20)), dtype = bool)
clean_and_dilated = ndimage.morphology.binary_dilation(clean_staff, \
													   structure,   \
													   iterations=50)
plt.imsave("spots_to_add.png", raw_staffs)
plt.imsave("without_repair.png", no_staff)
plt.imsave("repaired.png", no_staff+raw_staffs) 	
plt.imsave("cleaned_staff.png", clean_and_dilated)
pkl_name = "repaired_image.pkl"
with open(pkl_name, "wb") as f :
    pickle.dump({'repaired image':repaired_image, 'clean staff': clean_and_dilated}, f, pickle.HIGHEST_PROTOCOL)



