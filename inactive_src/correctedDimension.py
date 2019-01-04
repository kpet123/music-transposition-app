#ADAPTED FROM OPENCV COMPUTER VISION FOR FACES COURSE
#SCALE FACTOR IS NOT GLOBAL VARIABLE
#FOR NOW HARDCODED IN GET4POINTS AND RESIZE, EVENTURALLY APPLY TO ARRAY
#NOTE: UTILS CANNOT BE IMPORTED IN CURRENT FOLDER, MOVE TO RUN
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
            pts_dst.append([x*2,y*2])


if __name__ == '__main__' :
   # Read source image.
    im_src = cv2.imread('./strauss1.jpg')
    
    size = im_src.shape
    pts_dst = np.array([[0,0], 
                       [size[1]-1, 0], 
                       [size[1] - 1, size[0] -1],
                       [0, size[0] - 1 ]
                       ],dtype=float
                       );

    print('Click on four corners of the music and then press ENTER')
    pts_src = [] #points to be clicked
    cv2.namedWindow("Window",cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Window", get_four_points, pts_src)
    im_src_smaller = cv2.resize(im_src, None, \
    fx= .5, fy= .5, interpolation= cv2.INTER_LINEAR)
    
    cv2.imshow("Window", im_src_smaller)
    cv2.waitKey(0)
    #convert pts_src to array
    pts_src = np.asarray(pts_src)
    # Calculate Homography between source and destination points
    h, status = cv2.findHomography(pts_src, pts_dst);
    #create im_dst
    im_dst= np.copy(im_src)
    # Warp source image
    warped_image = cv2.warpPerspective(im_dst, h, (im_src.shape[1],im_src.shape[0]))

    cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
    # Display image.
    cv2.imshow("Image", warped_image);
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    cv2.imwrite("corrected_image.jpg", warped_image)
