#functions for haar image calculation, MUST REVERSE IMAGE TO COUNT BLACK PIXELS 
import cv2
import numpy as np



def hor_2(src, integral):
    rows = src.shape[0]
    cols =src.shape[1]
    #print src.shape
    top_val = integral[rows/2][cols]
    #print top_val
    bottom_val = integral[rows][cols]
    #print bottom_val
    difference = top_val-bottom_val
    return difference/255 #normalizes



def getHaarFeatures(src):
    src = ~src #reverse so integral image applies to black pixels
    integral = cv2.integral(src)
    feature_dict = {}

    #dictionary of features + feature value
    feature_dict = { 'hor_2':hor2(src, integral), \
                      }
    return feature_dict


#testing
def testing():
    imageName= "test_im/test0.png"
    im = ~cv2.imread(imageName, 0)
    integral = cv2.integral(im)
    print integral
    feature1 = haar_one(im, integral)
    print feature1
