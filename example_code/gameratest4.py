from gamera.core import *
init_gamera()


img = load_image("process_img.png")
img = img.to_onebit()
ccs = img.cc_analysis()
labels = [c.label for c in ccs]
for label in labels:
    print label

