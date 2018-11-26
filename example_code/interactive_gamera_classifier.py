#code from https://gamera.informatik.hsnr.de/docs/gamera-docs/script.html
#you can do this manually entirely thru gui, directions at
#       https://gamera.informatik.hsnr.de/docs/gamera-docs/training_tutorial.html



import sys

def my_application():
       global ccs

       # Load the image, and convert it to onebit
       image = load_image(sys.argv[-1])
       onebit = image.to_onebit()

       # Get the connected components from the image
       ccs = onebit.cc_analysis()

       # Classify the cc's
       classifier.classify_list_automatic(ccs)

       # Display the ccs to show their classification
       display_multi(ccs)

# Import the Gamera core and initialize it
from gamera.core import *
init_gamera()

# Import the classifier module
from gamera import knn
# Create a new classifier
classifier = knn.kNNInteractive()
# Load some training data
classifier.from_xml_filename("training.xml")

# Import the Gamera GUI and start it
from gamera.gui import gui
gui.run(my_application)




