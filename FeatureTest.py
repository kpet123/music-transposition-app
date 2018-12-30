#testing for features written by Kaitlin Pet
import cv2
import numpy


#define images

#horizontal half
im1 =numpy.array([  [0,  0,  0,  0,  0,  0,  0,  0], \
                    [0,  0,  0,  0,  0,  0,  0,  0],  \
                    [1., 1., 1., 1., 1., 1., 1., 1.],  \
                    [1., 1., 1., 1., 1., 1., 1., 1.]])
integral1=cv2.integral(im1)


#vertical half
im2 =numpy.array(  [[1., 1., 1., 1., 0, 0, 0, 0], \
                    [1., 1., 1., 1., 0, 0, 0, 0],  \
                    [1., 1., 1., 1., 0, 0, 0, 0],  \
                    [1., 1., 1., 1., 0, 0, 0, 0]])

integral2=cv2.integral(im2)

#diagnol
im3 =numpy.array([  [1., 1., 1., 1., 0,  0,  0,  0], \
                    [0,  1., 1., 1., 1., 0,  0,  0],  \
                    [0,  0,  1., 1., 1., 1., 0,  0],  \
                    [0,  0,  0,  0,  1., 1., 1., 1.]])

integral3 = cv2.integral(im3)

#quarters
im4 =numpy.array(  [[1.,  1.,  1.,  1.,  0,  0,  0,  0], \
                    [1.,  1.,  1.,  1.,  0,  0,  0,  0],  \
                    [0,   0,   0,   0,   1., 1., 1., 1.],  \
                    [0,   0,   0,   0,   1., 1., 1., 1.]])
integral4 = cv2.integral(im4)

#hollow
im5 =numpy.array(  [[1., 1., 1., 1., 1., 1., 1., 1.], \
                    [1., 0,  0,  0,  0,  0,  0,  1.],  \
                    [1., 0,  0,  0,  0,  0,  0,  1.],  \
                    [1., 1., 1., 1., 1., 1., 1., 1.]])
integral5 = cv2.integral(im5)

#solid middle
im6 =numpy.array([  [0, 0,  0,  0,  0,  0,  0,  0], \
                    [0, 1., 1., 1., 1., 1., 1., 0],  \
                    [0, 1., 1., 1., 1., 1., 1., 0],  \
                    [0, 0,  0,  0,  0,  0,  0,  0]])
integral6 = cv2.integral(im6)

#L
im7 =numpy.array(  [[1., 0,  0,  0,  0,  0,  0,  0], \
                    [1., 0,  0,  0,  0,  0,  0,  0],  \
                    [1., 0,  0,  0,  0,  0,  0,  0],  \
                    [1., 1., 1., 1., 1., 1., 1., 1.]])
integral7 = cv2.integral(im7)

######## list of images

image_list = [(im1, integral1), (im2, integral2), (im3, integral3), (im4, integral4), \
        (im5, integral5), (im6, integral6), (im7, integral7)]


def print_result(im_name, im, im_integral, function, true_result):

    print im_name
    
    result = function(im, im_integral, im.shape[0], im.shape[1])
    if result == true_result:
        print "\tPASS"
    else:
        print "\tFAIL: result should have been "+str(true_result)+" was "\
            + str(result)


#Testing haar features 
import haar as h


#TESTING h.hor_2
print "\n********TESTING h.hor_2********"


######im1
print_result("im1", im1, integral1, h.hor_2, 16)

######im2
print_result("im2", im2, integral2, h.hor_2, 0)

######im3
print_result("im3", im3, integral3, h.hor_2, 0)

######im4
print_result("im4", im4, integral4, h.hor_2, 0)

######im5
print_result("im5", im5, integral5, h.hor_2, 0)

######im6
print_result("im6", im6, integral6, h.hor_2, 0)

######im7
print_result("im7", im7, integral7, h.hor_2, 7)



#TESTING h.vert_2
print "\n********TESTING h.vert_2********"


######im1
print_result("im1", im1, integral1, h.vert_2, 0)

######im2
print_result("im2", im2, integral2, h.vert_2, -16)

######im3
print_result("im3", im3, integral3, h.vert_2, -2)

######im4
print_result("im4", im4, integral4, h.vert_2, 0)

######im5
print_result("im5", im5, integral5, h.vert_2, 0)

######im6
print_result("im6", im6, integral6, h.vert_2, 0)

######im7
print_result("im7", im7, integral7, h.vert_2, -3)




#TESTING h.hor_3
print "\n********TESTING h.hor_3********"


######im1
print_result("im1", im1, integral1, h.hor_3, 16)

######im2
print_result("im2", im2, integral2, h.hor_3, 8)

######im3
print_result("im3", im3, integral3, h.hor_3, 8)

######im4
print_result("im4", im4, integral4, h.hor_3, 8)

######im5
print_result("im5", im5, integral5, h.hor_3, 16)

######im6
print_result("im6", im6, integral6, h.hor_3, 0)

######im7
print_result("im7", im7, integral7, h.hor_3, 9)





#TESTING h.vert_3
print "\n********TESTING h.vert_3********"


######im1
print_result("im1", im1, integral1, h.vert_3, 4)

######im2
print_result("im2", im2, integral2, h.vert_3, 0)

######im3
print_result("im3", im3, integral3, h.vert_3, -2)

######im4
print_result("im4", im4, integral4, h.vert_3, 4)

######im5
print_result("im5", im5, integral5, h.vert_3, 8)

######im6
print_result("im6", im6, integral6, h.vert_3, 0)

######im7
print_result("im7", im7, integral7, h.vert_3, 5)



#TESTING h.quarters
print "\n********TESTING h.quarters********"

######im1
print_result("im1", im1, integral1, h.quarters, 0)

######im2
print_result("im2", im2, integral2, h.quarters, 0)

######im3
print_result("im3", im3, integral3, h.quarters, 10)

######im4
print_result("im4", im4, integral4, h.quarters, 16)

######im5
print_result("im5", im5, integral5, h.quarters, 0)

######im6
print_result("im6", im6, integral6, h.quarters, 0)

######im7
print_result("im7", im7, integral7, h.quarters, 1)






#### Testing im_functions

import im_functions

##Testing format_doc
