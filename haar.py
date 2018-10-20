#functions for haar image calculation, take image with 1 as black 0 as white 
import cv2
import numpy as np


#differenc between top and bottom half
def hor_2(src, integral, rows, cols):

    top_val = integral[rows/2][cols]# -0-0+0
    bottom_val = integral[rows][cols] - top_val #-0+0
    print bottom_val
    difference = bottom_val-top_val
    return difference 

#difference between right and left half
def vert_2(src, integral, rows, cols):

    left_val = integral[rows][cols/2]
    right_val = integral[rows][cols] - left_val
    difference = right_val - left_val
    return difference

#difference between middle and edges (horizontally)
def hor_3(src, integral, rows, cols):
    first_third = rows/3
    second_third = rows*2/3

    first_third_val = integral[first_third][cols]
    second_third_val = integral[second_third][cols] - first_third_val
    third_third_val = integral[rows][cols] - integral[second_third][cols]
    difference = first_third_val + third_third_val - second_third_val
    return difference

#difference between middle and edges (vertically)
def vert_3(src, integral, rows, cols):
    first_third = cols/3
    #print first_third
    second_third = cols*2/3
    #print second_third

    first_third_val = integral[rows][first_third]
    second_third_val = integral[rows][second_third] - first_third_val
    third_third_val = integral[rows][cols] - integral[rows][second_third]
    difference = first_third_val + third_third_val - second_third_val
    return difference

#    _ _ 
#   |x| |
#   | |x|
#    - - 
#space with x minus without x

def quarters(src, integral, rows, cols):
    hrows = rows/2
    hcols = cols/2

    topLeftQuarter = integral[hrows][hcols]
    topRightQuarter = integral[hrows][cols] - topLeftQuarter
    bottomLeftQuarter = integral[rows][hcols] - topLeftQuarter
    bottomRightQuarter = integral[rows][cols] - integral[hrows][cols] - integral[rows][hcols] \
            +topLeftQuarter

    return (topLeftQuarter+bottomRightQuarter)-(topRightQuarter+bottomLeftQuarter)
#    _ _ _
#   |x| |x|
#   | |x| |
#   |x| |x|
#    - - -
# space with x minus without x

#def checker1(src, integral, rows, cols): :#TODO implement


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
