#separates into different elements

import cv2
import numpy as np


## adapted from Opencv course
def displayConnectedComponents(im):
    imLabels = im

	# The following line finds the min and max pixel values
	# and their locations on an image.
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(imLabels)

	# Normalize the image so that the min value is 0 and max value is 255.
    imLabels = 255 * (imLabels - minVal)/(maxVal-minVal)

	# Convert image to 8-bits unsigned type
    imLabels = np.uint8(imLabels)

	# Apply a color map
    imColorMap = cv2.applyColorMap(imLabels, cv2.COLORMAP_JET)

	# Display colormapped labels
    cv2.imshow("Labels", imColorMap)
    cv2.imwrite("Labels.jpg", imColorMap)
    cv2.waitKey(0)
   
# Read image as grayscale
im = cv2.imread("./thresh.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Original", im)
# Threshold Image
th, imThresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)

# Find connected components
x, imLabels = cv2.connectedComponents(imThresh)

print "x is ", x
print "imThresh is ", type(imThresh)
# Display the labels
displayConnectedComponents(imLabels)


