# Copyright 2017 BIG VISION LLC ALL RIGHTS RESERVED
# 
# This code is made available to the students of 
# the online course titled "Computer Vision for Faces" 
# by Satya Mallick for personal non-commercial use. 
#
# Sharing this code is strictly prohibited without written
# permission from Big Vision LLC. 
#
# For licensing and other inquiries, please email 
# spmallick@bigvisionllc.com 
#

import cv2
import numpy as np
from utils import mouse_handler
from utils import get_four_points
import sys
import argparse

def get_four_points(action, x, y, flags, pts_dst):
    #define what happens with left mouseclick
    if action==cv2.EVENT_LBUTTONDOWN:
   
        if len(pts_dst)<4:
            pts_dst.append([x,y])


if __name__ == '__main__' :

    cardfile = sys.argv[1]
    destimagefile = sys.argv[2]
    im_src = cv2.imread(cardfile)
    im_dst = cv2.imread(destimagefile)

    size = im_src.shape
    # Create a vector of source points.
    pts_src = np.array(
                       [
                        [0,0],
                        [size[1] - 1, 0],
                        [size[1] - 1, size[0] -1],
                        [0, size[0] - 1 ]
                        ],dtype=float
                       );

    #try pts_dst as list
    pts_dst=[]
    
       # Get four corners of the billboard
    print('Click on four corners of a billboard and then press ENTER')

    cv2.namedWindow("Window",cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Window", get_four_points, pts_dst)
    cv2.imshow("Window", im_dst)
    cv2.waitKey(0)
    #convert pnts_dst to arrau
    pts_dst = np.asarray(pts_dst)
    # Calculate Homography between source and destination points
    h, status = cv2.findHomography(pts_src, pts_dst);
    # Warp source image
    im_temp = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

    # Black out polygonal area in destination image.
    cv2.fillConvexPoly(im_dst, pts_dst.astype(int), 0, 16);
    
    # Add warped source image to destination image.
    im_dst = im_dst + im_temp;
    cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
    # Display image.
    cv2.imshow("Image", im_dst);
    cv2.waitKey(0);
    cv2.destroyAllWindows()
