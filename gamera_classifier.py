#code from https://gamera.informatik.hsnr.de/docs/gamera-docs/script.html


import sys
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
STAFF_HEIGHT=2 #int(sys.argv[2])
onebit = image.to_onebit()

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
#lists for different types
for c in component_list:
    guess = classifier.guess_glyph_automatic(c)
#    print guess
    if  guess[0][0][0] > .015:
        c.classify_heuristic(guess[0][0][1])
    else:
        c.classify_heuristic("unclassified")

#    c.save_PNG("guess.png")
#    eval = raw_input()
# Display the ccs to show their classification
#display_multi(classifiedimgs)

#Inspect performance in GUI
gamera_xml.glyphs_to_xml("knn-results.xml", component_list, False)



