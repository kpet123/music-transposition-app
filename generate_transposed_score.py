#at this point just generates shifted score, 
#TODO: incorporate accidental identification and change into workflow

import ScoreManipulation as scorem
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys


def system_processing(system_features, direction, displacement, thickness):

			#system with staff lines removed
			no_staff = system_features['no_staff_img']

			#only staff lines in the system 
			just_staff = system_features['just_staff_img']
			
			#get staff locations and distance between each staffline
			line_locations, gapsize = scorem.get_system_staff_location(just_staff)

			#repair 
			repaired_no_staff, repaired_just_staff = scorem.fill_gaps(just_staff, no_staff, thickness)

			#move staff lines
			shifted_system = scorem.movelines(repaired_no_staff, repaired_just_staff, displacement, direction)
			
			return shifted_system


def main():

		score = mpimg.imread(sys.argv[1]) #must be png
		displacement = int(sys.argv[2]) #amount to be shifted
		direction = sys.argv[3] #move staff 'up' or 'down'
		#convert to manipulable format
		score = scorem.format_doc(score)

		#get thickness of staff 
		ver_run_histogram = scorem.get_run_histogram(score, "vertical")
		thickness = scorem.find_histogram_max(ver_run_histogram)

		#get list of dictionaries of staff features 
		staff_list = scorem.get_staff_cc(score, sep_function = scorem.staff_separation)

		new_score = scorem.generate_score(score, staff_list, system_processing, direction, displacement, thickness)
		plt.imsave("new_score.png", new_score)


main()
