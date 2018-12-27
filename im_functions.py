#module with image functions for dealing with 2D doctypes
#reimplentation of certain gamera functions with numpy


import numpy as np
import itertools


#************** format_doc(arr) *************************

#converts numpy array of floats and zeros
# to 1s and 0s with 1s representing black
def format_doc(arr):
	max_val = np.amax(arr)
	arr = arr/max_val #converts to ones and zeros
	arr = arr.astype(bool) #converts to boolean
	arr =(~arr).astype(int) #flip bits and cast to int
	return arr

#********************* runs_of_ones(boolArr) **********************

#returns list, each element is length of a run in bitArr
#bitArr is  1D array/list of 1s and 0s
#adapted from : https://stackoverflow.com/questions/1066758/find-length-of-sequences-of-identical-values-in-a-numpy-array-run-length-encodi

def runs_of_ones(bitArr):
	run_list = []
	for key, run_group  in itertools.groupby(bitArr):
		if key: run_list.append(sum(run_group))  
	return run_list
			

#******** get_runs_histogram(arr, orientation_str, val_to_count) ********

#generates histogram (list) of runs existing in document
#position in list indicates length of run
#value at position indicates number of occurences 
#	arr = input document as numpy array
#	orientation_str = "horizontal", "vertical"
#	val_to_count = number (int/float) value of element making up run
#		right now only works as 1 bc otherwise run_of_ones()
#		 will crash, work on fixing in future 
#	
def get_most_freqent_run(arr, orientation_str, val_to_count=1):
	
	
	arr = arr.astype(int)
	
	if orientation_str == "horizontal":
		histogram = []
		rownum = 0
		while rownum < len(arr)
			row = arr[rownum]
			histogram = histogram + runs_of_ones(row)
			rownum = rownum + 1
			
		
		
	elif orientation_str == "vertical":
	
	else: 
		#throw error
		print( "orientation must be 'horizontal' or 'vertical'")

	
