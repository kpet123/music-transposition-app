#at this point just generates shifted score, 
#TODO: incorporate accidental identification and change into workflow

import ScoreManipulation as scorem
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def system_processing(system_features):

			#system with staff lines removed
			no_staff = system_features['no_staff_img']

			#only staff lines in the system 
			just_staff = system_features['just_staff_img']
			
			#get staff locations and distance between each staffline
			line_locations, gapsize = get_system_staff_location(just_staff)

			#repair 
			repaired_no_staff, repaired_just_staff = fill_gaps(just_staff, no_staff, thickness)

			#move staff lines
			shifted_system = movelines(no_staff, just_staff, DISPLACEMENT, DIRECTION)
			
			return shifted_system


def main():

		score = mpimg.imread(sys.argv[1]) #must be png

		#convert to manipulable format
		score = scorem.format_doc(score)

		#get thickness of staff 
		ver_run_histogram = scorem.get_run_histogram(score, "vertical")
		thickness = scorem.find_histogram_max(ver_run_histogram)

		#get list of dictionaries of staff features 
		staff_list = scorem.get_staff_cc(score, sep_function = scorm.staff_separation)
	
		#generated edited systems
		i=0
		while i < len(staff_list):
			
			#extract feature dictionary
			system_features = staff_list[i]

			#produced system with shifted stafflines
			altered_system = system_processing(system_features)
	
			#add to system_features
			system_features['altered system'] = altered_system

			#replace with original
			staff_list[i] = system_features
					
			#iterate
			i = i+1


	new_score = scorem.generate_score(score, staff_list, system_processing)
