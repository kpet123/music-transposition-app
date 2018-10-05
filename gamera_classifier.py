#code from https://gamera.informatik.hsnr.de/docs/gamera-docs/script.html


import sys
# Import the Gamera core and initialize it
from gamera.core import *
init_gamera()

# Import the classifier module
from gamera import knn

def main():
    # Create a new classifier, figure out feature u like 
    classifier = knn.kNNNonInteractive([],
            ["aspect ratio","moments","volume64regions","nrows feature"], 0,normalize=True)
    # Load training data
    classifier.from_xml_filename("knn_glyphs.xml")


    # Load the image, and convert it to onebit
    image = load_image(sys.argv[-1])
    onebit = image.to_onebit()

    # Get the connected components from the image
    component_list = onebit.cc_analysis()
    
    #classify images choose grouping function
    classifiedimgs = classifier.group_and_update_list_automatic(component_list, \
            ShapedGroupingFunction(STAFF_HEIGHT), max_parts_per_group=2)

    # Display the ccs to show their classification
    display_multi(classifiedimgs)




main()
