#code from https://gamera.informatik.hsnr.de/docs/gamera-docs/script.html

import haar as h
import sys
import cv2
# Import the Gamera core and initialize it
from gamera.core import *
# Import the classifier module
from gamera import knn
from gamera.classify import ShapedGroupingFunction
from gamera import gamera_xml
init_gamera()




# Create a new classifier, figure out feature u like 
classifier = knn.kNNNonInteractive("./classifiers/knnFullSymbolGlyphs.xml",
        ["aspect_ratio","moments","compactness", "fourier_broken", "volume16regions","nholes"], 0,normalize=True)
# Load training data
#classifier.from_xml_filename("knn_glyphs.xml")


# Load the image, and convert it to onebit

image = load_image(sys.argv[-1])
onebit = image.to_onebit()
STAFF_HEIGHT=2 #int(sys.argv[2])

# Get the connected components from the image
component_list = onebit.cc_analysis()

print len(component_list)

### WITH GROUPING

#classify images choose grouping function
#possible use for exclusively flats, haven't encountered split versions of other characters
#classifiedimgs = classifier.group_and_update_list_automatic(component_list, \
#        grouping_function=ShapedGroupingFunction(4),\
#        max_parts_per_group=2)

### WITHOUT GROUPING

size_predictor = []
# Determine size of components using glyph guessing
for c in component_list:

    #
    guess = classifier.guess_glyph_automatic(c)
#    print guess
    if  guess[0][0][0] > .015:
        sz = c.ncols * c.nrows
        size_predictor.append(sz)
 

candidates = [] #for glyphs conforming to average size
for c in component_list:
    size = c.ncols*c.nrows 
    if size > min(size_predictor)*.5 and size < max(size_predictor)*2: #rule out by size
        arr = c.to_numpy()
        candidates.append(arr)


#test haar

for arr in candidates:
    print type(arr)
    arr = ~arr
    print arr.shape
    cv2.imshow("image", arr)
    cv2.waitKey(0)
    integral = cv2.integral(arr)
    print h.hor_2(arr, integral)


# Display the ccs to show their classification
#display_multi(classifiedimgs)

#Inspect performance in GUI
gamera_xml.glyphs_to_xml("knn-results.xml", component_list, False)



