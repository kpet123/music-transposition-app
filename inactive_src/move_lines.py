#moves lines to specified position

#parames
DISPLACEMENT = 2  #how far to move note
DIRECTION = 'up'
#
import im_functions
import pickle
import numpy as np
import matplotlib.pyplot as plt

with open("systems.pkl", "rb") as f:
    systems = pickle.load(f)
#extract from pickle
system = systems[0]
no_staff = system['no_staff_img']
just_staff = system['just_staff_img']

#test fill_gaps()

no_staff, just_staff = im_functions.fill_gaps(just_staff, no_staff, 1)

#copy from here

#find distance corresponding to shifting 1 note
staff_locations, gapsize =\
              im_functions.get_system_staff_location(just_staff)
note_dist = gapsize/2

#TODO: correct just_staff?

#block to add:

print("note_dist : ", note_dist)
print("displacement: ", DISPLACEMENT)
print("size of no_staff[0]", len(no_staff[0])) 
block = np.zeros((int(note_dist*DISPLACEMENT), len(no_staff[0])))

if DIRECTION == 'up':
	#shift staff up
	staff_block = np.concatenate((just_staff, block))
	#shift music down
	no_staff_block = np.concatenate((block, no_staff))
	#add so staff is shifted up relative to music
	shifted_system = staff_block + no_staff_block

elif DIRECTION == 'down':
	staff_block = np.concatenate((block, just_staff))
	no_staff_block = np.concatenate((no_staff, block))
	shifted_system = staff_block + no_staff_block
	#add so staff is shifted up relative to music
	shifted_system = staff_block + no_staff_block

else:
	raise ValueError("Direction must be up or down")


plt.imsave("staff_block", staff_block)
