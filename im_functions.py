#module with image functions for dealing with 2D doctypes
#reimplentation of certain gamera functions with numpy


import numpy as np
import itertools

'''
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
'''
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
	print("run lengths")
	print(runlengths)
	print("run starts")
	print(run_starts)
	return runlengths, run_starts

'''
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

'''
*********** isolate_run(arr, target_val, replace_val, orientation_str) ***

replaces runs longer and shorter than target_val with replace_val
'''	
def isolate_run(arr, target_val, replace_val, orientation_str):
	if orientation_str == "horizontal":
		rownum = 0
		while rownum < len(arr):
			row = arr[rownum]
			runlengths, runstarts = find_runs(row)
			#replace non_target rows with replace_val
			i = 0
			while i< len(runlengths):
				print(runlengths[i])
				if runlengths[i] != target_val:
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
				if runlengths[i] != target_val:
					#TODO: optimize replacement! lookup table?
					j = runstarts[i]
					print("run starts at", runstarts[i])
					print("run ends at", runlengths[i]+runstarts[i])
					while j<runlengths[i]+runstarts[i]:
						arr[j][colnum] = replace_val
						j = j+1
					 
				i = i+1	
			colnum = colnum + 1
		return arr	
	else:
		raise ValueError("orientation must be 'horizontal' or 'vertical")
