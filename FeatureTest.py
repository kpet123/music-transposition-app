#testing for features written by Kaitlin Pet
import cv2
import numpy


#define images

#horizontal half
im1 =numpy.array([[0, 0, 0, 0, 0, 0, 0, 0], \
                    [0, 0, 0, 0, 0, 0, 0, 0],  \
                    [1, 1, 1, 1, 1, 1, 1, 1],  \
                    [1, 1, 1, 1, 1, 1, 1, 1]])
integral1=cv2.integral(im1)


#vertical half
im2 =numpy.ndarray([[1, 1, 1, 1, 0, 0, 0, 0], \
                    [1, 1, 1, 1, 0, 0, 0, 0],  \
                    [1, 1, 1, 1, 0, 0, 0, 0],  \
                    [1, 1, 1, 1, 0, 0, 0, 0]])

integral2=cv2.integral(im2)

#diagnol
im3 =numpy.ndarray([[1, 1, 1, 1, 0, 0, 0, 0], \
                    [0, 1, 1, 1, 1, 0, 0, 0],  \
                    [0, 0, 1, 1, 1, 1, 0, 0],  \
                    [0, 0, 0, 0, 1, 1, 1, 1]])

integral3 = cv2.integral(im3)

#quarters
im4 =numpy.ndarray([[1, 1, 1, 1, 0, 0, 0, 0], \
                    [1, 1, 1, 1, 0, 0, 0, 0],  \
                    [0, 0, 0, 0, 1, 1, 1, 1],  \
                    [0, 0, 0, 0, 1, 1, 1, 1]])
integral4 = cv2.integral(im4)

#hollow
im5 =numpy.ndarray([[1, 1, 1, 1, 1, 1, 1, 1], \
                    [1, 0, 0, 0, 0, 0, 0, 1],  \
                    [1, 0, 0, 0, 0, 0, 0, 1],  \
                    [1, 1, 1, 1, 1, 1, 1, 1]])
integral5 = cv2.integral(im5)

#solid middle
im6 =numpy.ndarray([[0, 0, 0, 0, 0, 0, 0, 0], \
                    [0, 1, 1, 1, 1, 1, 1, 0],  \
                    [0, 1, 1, 1, 1, 1, 1, 0],  \
                    [0, 0, 0, 0, 0, 0, 0, 0]])
integral6 = cv2.integral(im6)

#L
im7 =numpy.ndarray([[1, 0, 0, 0, 0, 0, 0, 0], \
                    [1, 0, 0, 0, 0, 0, 0, 0],  \
                    [1, 0, 0, 0, 0, 0, 0, 0],  \
                    [1, 1, 1, 1, 1, 1, 1, 1]])
integral7 = cv2.integral(im5)

######## list of images

image_list = [(im1, integral1), (im2, integral2), (im3, integral3), (im4, integral4), \
        (im5, integral5), (im6, integral6), (im7, integral7)]


#Testing haar features 
import haar as h


#TESTING h.hor_2
######im1
if h.hor2(im1, integral1, im1.shape[0], im1.shape[1]) == 16:
    print "PASS: h.hor2 passes im1"
else:
    print "FAIL: h.hor2 fails im1"

######im2
if h.hor2(im2, integral2, im2.shape[0], im2.shape[1]) == 0:
    print "PASS: h.hor2 passes im2"
else:
    print "FAIL: h.hor2 fails im2"


######im3
if h.hor2(im3, integral3, im3.shape[0], im3.shape[1]) == 0:
    print "PASS: h.hor2 passes im3"
else:
    print "FAIL: h.hor2 fails im3"



######im4
if h.hor2(im4, integral4, im4.shape[0], im4.shape[1]) == 0:
    print "PASS: h.hor2 passes im4"
else:
    print "FAIL: h.hor2 fails im4"


######im5
if h.hor2(im5, integral5, im5.shape[0], im5.shape[1]) == 0:
    print "PASS: h.hor2 passes im5"
else:
    print "FAIL: h.hor2 fails im5"



######im6
if h.hor2(im6, integral6, im6.shape[0], im6.shape[1]) == 0:
    print "PASS: h.hor2 passes im6"
else:
    print "FAIL: h.hor2 fails im6"



#h.vert2


#h.hor_3

#h.vert3


#h.quarters






