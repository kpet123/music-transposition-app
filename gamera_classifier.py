#code from https://gamera.informatik.hsnr.de/docs/gamera-docs/script.html


import sys
# Import the Gamera core and initialize it
from gamera.core import *
# Import the classifier module
from gamera import knn
from gamera import classify
from gamera import gamera_xml
init_gamera()




# Create a new classifier, figure out feature u like 
classifier = knn.kNNNonInteractive("knn_glyphs.xml",
        ["aspect_ratio","moments","volume64regions","nrows_feature"], 0,normalize=True)
# Load training data
#classifier.from_xml_filename("knn_glyphs.xml")


# Load the image, and convert it to onebit
image = load_image(sys.argv[-1])
STAFF_HEIGHT=2 #int(sys.argv[2])
onebit = image.to_onebit()

# Get the connected components from the image
component_list = onebit.cc_analysis()

#classify images choose grouping function
classifiedimgs = classifier.group_and_update_list_automatic(component_list, \
  #      grouping_function=BoundingBoxGroupingFunction(2),\
        max_parts_per_group=2)

# Display the ccs to show their classification
#display_multi(classifiedimgs)

#Inspect performance in GUI
gamera_xml.glyphs_to_xml("knn-results.xml", classifiedimgs, False)



