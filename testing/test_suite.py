#testing for features written by Kaitlin Pet
#import cv2
import numpy as np
import test_ims
import im_functions
	
def print_result(im_name, function, true_result , equality_function, *args):

   print( im_name)
    
   result = function(*args)
   if equality_function(result, true_result):
        print( "\tPASS")
   else:
        print( "\tFAIL: result should have been "+str(true_result)+" was "\
            + str(result))



def get_run_histogram_test():
	print("TESTING get_run_histogram()")
	im_list = test_ims.small_images()
	equality_function=np.array_equal
	#image0
	
	#horizontal, 1
	true_result = np.array([0,0,0,0,0,0,0,0,2] )
	print_result("im0-horizontal", im_functions.get_run_histogram,\
 true_result, equality_function, im_list[0],"horizontal")

	#vertical, 1
	true_result =np.array([0,0,8])
	print_result("im0-vertical", im_functions.get_run_histogram, true_result, \
equality_function, im_list[0], "vertical")
	#horizontal, 0

	#vertical, 0


def test_isolate_run()
		im2=test_ims.small_images()[2]
		print(im2)
		arr = im_functions.isolate_run(im2, 2, 0, "vertical")
		print(arr)
		arr2 = im_functions.isolate_run(im2, 2, 0, "horizontal")
		print(arr2)

		arr3 = im_functions.isolate_run(im2, 2, 0, "horiz")

		print(arr3)



def main():
	get_run_histogram_test()

main()

