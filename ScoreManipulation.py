#module with image functions for dealing with 2D doctypes
#reimplentation of certain gamera functions with numpy


import numpy as np
import itertools
import sys
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 
import scipy.ndimage as ndimage
import pickle 
import math
from skimage import measure

'''TESTED
************** format_doc(arr) *************************

converts numpy array of floats and zeros
to 1s and 0s with 1s representing black
'''


def format_doc(arr):
	max_val = np.amax(arr)
	arr = arr/max_val #converts to ones and zeros
	arr = arr.astype(bool) #converts to boolean
	arr =(~arr).astype(int) #flip bits and cast to int
	return arr



'''TESTED
********************* runs_of_ones(boolArr) **********************

-returns list, each element is length of a run in bitArr
-bitArr is  1D array/list of 1s and 0s
-adapted from : https://stackoverflow.com/questions/1066758/find-length-of-sequences-of-identical-values-in-a-numpy-array-run-length-encodi

'''
def runs_of_ones(bitArr):
	run_list = []
	for key, run_group  in itertools.groupby(bitArr):
		if key: run_list.append(sum(run_group))  
	return run_list
			
#more robust
def find_runs(arr):
	# make sure all runs of ones are well-bounded
	bounded = np.hstack(([0], arr, [0]))
	# get 1 at run starts and -1 at run ends
	difs = np.diff(bounded)
	run_starts, = np.where(difs > 0)
	run_ends, = np.where(difs < 0)
	runlengths =  run_ends - run_starts
	return runlengths, run_starts

'''TESTED
******** get_runs_histogram(arr, orientation_str, val_to_count) ********

-generates histogram (list) of runs existing in document
-position in list indicates length of run
-value at position indicates number of occurences 
	arr = input document as numpy array
	orientation_str = "horizontal", "vertical"
	val_to_count = number (int/float) value of element making up run
'''


def get_run_histogram(arr, orientation_str, val_to_count=1):
	
	
	arr = arr.astype(int)
	
	if orientation_str == "horizontal":
		histogram = []
		rownum = 0
		while rownum < len(arr):
			row = arr[rownum]
			histogram = histogram + runs_of_ones(row)
			rownum = rownum + 1
		return np.bincount(histogram)			
		
		
	elif orientation_str == "vertical":
		histogram = []
		colnum = 0
		while colnum < len(arr[1]):
			col = arr[:,colnum]
			histogram = histogram + runs_of_ones(col)
			colnum = colnum +1
		return np.bincount(histogram)
	
	else: 
		raise ValueError("orientation must be 'horizontal or 'vertical'")



'''TESTED
*********** isolate_run(arr, target_val, replace_val, orientation_str) ***

replaces runs longer and shorter than target_val with replace_val
'''	
def isolate_run(arr, target_val, replace_val, orientation_str, thresh=0):
	if orientation_str == "horizontal":
		rownum = 0
		while rownum < len(arr):
			row = arr[rownum]
			runlengths, runstarts = find_runs(row)
			#replace non_target rows with replace_val
			i = 0
			while i< len(runlengths):
				print(runlengths[i])
				if not(target_val - thresh <= runlengths[i] <=  target_val + thresh):
					#TODO: optimize replacement! lookup table?
					j = runstarts[i]
					while j<runlengths[i]+runstarts[i]:
						arr[rownum][j] = replace_val
						j = j+1
					 
				i = i+1	
			rownum = rownum + 1
		return arr
	
	elif orientation_str == "vertical":
		colnum = 0
		while colnum < len(arr[0]):
			col = arr[:, colnum]
			runlengths, runstarts = find_runs(col)
			#replace non_target rows with replace_val
			i = 0
			while i< len(runlengths):
				if not(target_val - thresh <= runlengths[i] <=  target_val + thresh):
					#TODO: optimize replacement! lookup table?
					j = runstarts[i]
					while j<runlengths[i]+runstarts[i]:
						arr[j][colnum] = replace_val
						j = j+1
					 
				i = i+1	
			colnum = colnum + 1
		return arr	
	else:
		raise ValueError("orientation must be 'horizontal' or 'vertical")


'''
finds most frequent element in histogram

Input: 1D histogram array with value as index and frequency of value as value associated with index

Output: (int) most frequent element (index)
'''
def find_histogram_max(proj_arr):
		most_frequent_occurences = max(proj_arr) # number of occurences

		#value corresponds to height of staff line, may also remove parts of slurs
		value = np.where(proj_arr == most_frequent_occurences)[0]
		return value



'''TESTED
version of gameraStaffRemoval.py without gamera functions. 
input - png file of sheet music (sys.argv[0])
output - file with just staffs and file with music-staffs (filenames 
	     specified as sys.argv[1] and sys.argv[2], respectively

TODO: make it safe

'''

def staff_separation(img):

		proj_arr= get_run_histogram(img, "vertical")
		most_frequent_occurences = max(proj_arr) # number of occurences

		#value corresponds to height of staff line, may also remove parts of slurs
		value = np.where(proj_arr == most_frequent_occurences)[0]

		img2 = np.copy(img) #isolate_run mutates original
		verticalStaffs = isolate_run(img2, value, 0, "vertical", thresh=1)

		no_staff_raw = img - verticalStaffs

		return verticalStaffs, no_staff_raw


'''

Adapted from gamera_getCC.py
Gets connected compnents from sheet music file then pickles
Input: 
	formatted_img: array formatted with format_doc
	pkl: str of whether or not to pickle return, "yes" or "no"
Ouput:
	list of dictionaries. Each dictionary has the features:
		staff: (numpy arr) slice of formatted_img containing staff
		no_staff_img: (numpy arr) staff with stafflines removed
		just_staff_img: (numpy arr) staff with everything other than stafflines removed
		offset_x: (int) x offset of staff bounding box -rc
		offset_y:(int)  y offset of staff bounding box -rc
		all_features: dictionary of other features generated by measure.regionprops()
		
'''
def get_staff_cc(img, sep_function = staff_separation, pkl = "no", pkl_name = None):


		#arr with different values labeling each cc
		blob_img = measure.label(img)

		#list of ccs and their attributes
		component_list = measure.regionprops(blob_img)
		system_list = [] #list with all system info
		
		#generate system_list
		for c in component_list:
		   
			#find systems, rule out by size
			if c['bbox_area'] > len(img[0])* len(img)/100:
				bbox=c['bbox']
				#remove staff in system
				c_staff, c_nostaff = sep_function(img[bbox[0]:bbox[2],\
									  bbox[1]:bbox[3]])
				system_list.append({"staff":img[bbox[0]:bbox[2],bbox[1]:bbox[3]],\
									"no_staff_img" : c_nostaff,\
									"just_staff_img" : c_staff,\
									"offset_x" : bbox[1], \
									"offset_y" : bbox[0],\
									"all_features" : c})
		 
		if pkl == "yes":
				with open(pkl_name, "wb") as f : 
					pickle.dump(system_list, f, pickle.HIGHEST_PROTOCOL)

		return system_list

'''TESTED
Uses gradient shifts in horizontal staff projection to cacluate staff location
Input: 1D numpy array of staff horizontal projection
Output: sorted list of staff locations
'''

def gradientloc(staffs1D):
    #enumerate staffs1D and delete areas where there is no data 
    bounded = np.hstack(([0], staffs1D, [0]))
    staff_gradient=np.diff(bounded)
    staff_gradient=list(staff_gradient)
    staff_features = []
    i=0
    while i< len(staff_gradient):
        staff_features.append([i, staff_gradient[i]])
        i+=1

  
    #sort by gradient value
    sort_gradient = sorted(staff_features, key=lambda tup: tup[1])
    #highest gradients should correspond to biggest jumps; i.e. beginning of line
    lines = sort_gradient[len(sort_gradient)-5 :len(sort_gradient)]
    #convert to array to slice x values
    linelocs= np.array(lines)[:,0]
    #sort 
    return sorted(linelocs)

'''TESTED
Gives coordinates of degraded horizontal lines  within an image and distances between them

Input:
	staff_arr: array with only staff lines (1 system)
Output: 
	locations of staff lines (numpy array)
'''



def get_system_staff_location(staff_arr):

	#get 1D projection
	staffs1D = np.sum(staff_arr, axis=1)

	#pick method
	staff_locations = np.asarray(gradientloc(staffs1D)) 
    
    #calculate size of gaps
	gapsize = np.average(np.diff(staff_locations))

	return staff_locations, gapsize



'''TESTED
# replaces areas deleted in staff removal
Input:
    raw_staffs: formatted array of just staffs
    no_staff: formatted array of music with staffs removed
    thickness: thickness of staff line
    pkl: if pickled result of output wanted, 'yes' or 'no'
    pkl_name: name of pickle file with .pkl extension
Output:
    repaired system without stafflines
	cleaned+dilated
'''
def fill_gaps(raw_staffs, no_staff, thickness, pkl='no', pkl_name=None):

		#variables needed
		raw_staff_copy = np.copy(raw_staffs)
		spots_to_repair = raw_staffs
		staff_width = len(raw_staffs[0])
		thickness = int(thickness)

		#caculate staff locations 
		staff_locations, d = get_system_staff_location(raw_staffs)

		#array of zeros for blanking out staff lines
		blockspace = np.zeros((thickness, staff_width))
		#blank every staff line
		for location in staff_locations:
			spots_to_repair[location:location+thickness, 0:staff_width] = \
																blockspace
		#add 
		repaired_image = no_staff + spots_to_repair


		#generate clean staff image
		clean_staff = raw_staff_copy - spots_to_repair
		structure = np.ones((thickness, int(staff_width/20)), dtype = bool)
		clean_and_dilated = ndimage.morphology.binary_dilation(clean_staff, \
															   structure,   \
															   iterations=50)
		if pkl == 'yes':
				with open(pkl_name, "wb") as f :
					pickle.dump({'repaired image':repaired_image, 'clean staff': clean_and_dilated}, f, pickle.HIGHEST_PROTOCOL)

		#plt.imsave("repaired_image.png", repaired_image)
		#plt.imsave("clean_and_dilated.png", clean_and_dilated)
		return repaired_image, clean_and_dilated



'''
#moves lines to specified position
'''



def movelines(no_staff, just_staff, displacement, direction, plk='no', pklname='None'):

		#find distance corresponding to shifting 1 note
		staff_locations, gapsize = get_system_staff_location(just_staff)
		note_dist = gapsize/2


		#block to add:
		block = np.zeros((int(note_dist*displacement), len(no_staff[0])))

		if direction == 'down':

			#shift staff up
			staff_block = np.concatenate((just_staff, block))
			#shift music down
			no_staff_block = np.concatenate((block, no_staff))
			#add so staff is shifted up relative to music
			shifted_system = staff_block + no_staff_block

		elif direction == 'up':
			staff_block = np.concatenate((block, just_staff))
			no_staff_block = np.concatenate((no_staff, block))
			shifted_system = staff_block + no_staff_block
			#add so staff is shifted up relative to music
			shifted_system = staff_block + no_staff_block

		else:
			raise ValueError("'direction' must be 'up' or 'down'")

		#plt.imsave("staff_block.png", staff_block)
		return shifted_system


'''
generates score 
Input:
	score: (numpy arr) plt loaded and formatted version of original score
	staff_list: list of dictionary generated by get_staff_cc() from score
	alter_func: function used to generate altered systems for the new score
'''

def generate_score(score, staff_list, alter_func, *args):

	#generated edited staff_list
	i=0
	while i < len(staff_list):
	
		#extract feature dictionary
		system_features = staff_list[i]

		#produced system with shifted stafflines
		altered_system = alter_func(system_features, *args)

		#add to system_features
		system_features['altered system'] = altered_system

		#replace with original
		staff_list[i] = system_features
			
		#iterate
		i = i+1

	#generate array of the new score
	score_width = len(score[0])
	fst_offset_y = staff_list[0]["offset_y"]
	top_slice = score[0: fst_offset_y, 0:score_width]

	i=0
	while i < len(staff_list):
		
		#get altered system
		altered_system = staff_list[i]['altered system']
		height = len(altered_system)

		#calculate length of buffer on both sides
		total_buff_len = score_width - len(altered_system[0])
		half_buf_len = total_buff_len/2 #this is float
		#ensure right and left buffer at up to correct length
		right_buff_len = math.floor(half_buf_len + 1)
		left_buff_len = math.ceil(half_buf_len - 1)

		#create right and left buffer
		right_buff = np.zeros((height, right_buff_len))
		left_buff = np.zeros((height, left_buff_len))

		#add right and left buffer to altered_system
		buffered_altered_system = np.hstack((left_buff, altered_system, right_buff))
		
		#concat	
		top_slice = np.concatenate((top_slice, buffered_altered_system))
		
		#iterate
		i = i+1
		

	#calculate where footer of score starts
	lst_staff = staff_list[len(staff_list)-1]
	lst_y_offset = lst_staff['offset_y']
	lst_staff_height = len(lst_staff['no_staff_img'])
	final_offset_y = lst_y_offset + lst_staff_height

	#concat footer of score

	footer = score[final_offset_y:len(score), 0: score_width]
	top_slice = np.concatenate((top_slice, footer))


	return top_slice

    
	
