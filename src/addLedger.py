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

if DIRECTION == 'down':
	#shift staff up
	staff_block = np.concatenate((just_staff, block))
	#shift music down
	no_staff_block = np.concatenate((block, no_staff))
	#add so staff is shifted up relative to music
	shifted_system = staff_block + no_staff_block

elif DIRECTION == 'up':
	staff_block = np.concatenate((block, just_staff))
	no_staff_block = np.concatenate((no_staff, block))
	shifted_system = staff_block + no_staff_block
	#add so staff is shifted up relative to music
	shifted_system = staff_block + no_staff_block

else:
	raise ValueError("Direction must be up or down")





#adds ledger lines to notes moved out of range in movelines()




EXTREME_LINE_LOCATION= staff_locations[0]+ int(note_dist*DISPLACEMENT)
DIRECTION = DIRECTION
GAPSIZE = gapsize
SHIFTED_SYSTEM = shifted_system
THICKNESS = 1

if DIRECTION == 'up':
	#slice shifted_system to get only part to analyze
	upper_slice = shifted_system[0:EXTREME_LINE_LOCATION, 0: len(SHIFTED_SYSTEM[0])]
	
	#extract locations staff lines would be 
	test_length = 3*THICKNESS
	


