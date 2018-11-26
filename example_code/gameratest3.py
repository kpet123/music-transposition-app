import sys
from gamera.core import *
init_gamera()

img = load_image("process_img.png")
img = img.to_onebit()
proj_arr = img.run_histogram("black", "vertical")

most_frequent_occurences = max(proj_arr) # number of occurences
print most_frequent_occurences
value = proj_arr.index(most_frequent_occurences)#length of rune
print value

filter1 = img.image_copy()

#img will only have most frequent rune 
filter1.filter_short_runs(value, "black")
filter1.filter_tall_runs(value, "black")

filter1.save_PNG("filter.png")
rgb = img.to_rgb()
rgb.highlight(filter1, RGBPixel(255,0,0))
rgb.save_PNG("highight.png")

