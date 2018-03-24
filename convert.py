#Note: in Image, im.getpixel((x,y)) is (columns traversed, rows traversed)
#in array, array[x,y] is [rows traversed, columns traversed]
#so need to switch x and y for program to function

#STEP 1
#PURPOSE: convert raw jpg file to clean binary uint8 black and white jpg

#### Outside libraries
import numpy as np
import cv2
import time
import sys
import argparse
import cPickle as cpickle
#### Other Modules
#### Constants

SCALEFACTOR=255 #easier to do calculation with black=1 then convert back
TSCALE = 80  #minimum allowable theta value in hough line transform
TRANGE = 20  #range that 'horizontal' line can encompas in hough line trasform
GAP = 15    #used in hor_lines, absolute distance in pixels between each pixel checked
PERCENT_COVERAGE = .75 # percent of entire page a staff horizonally takes up...will be changed

sys.setrecursionlimit(50000)


## collection of different methods to apply to image to make more clear


def dialate(img):
    kernel = np.ones((2,2), np.uint8)
    dilated_im = cv2.dilate(img, kernel, iterations = 1)
    cv2.imshow("dilated image", dilated_im)
    cv2.imwrite("di.jpg", dilated_im)  
    return dilated_im


def gaussian_blur(img):
    # 5x5 kernel, (0,0) implies sigma calculated automatically
    gauss_im=cv2.GaussianBlur(img,(5,5),0,0)
    cv2.imshow("Gaussian Blur", gauss_im)
    cv2.waitKey(0)
    cv2.imwrite("gaussian.jpg", gauss_im)
    return gauss_im

def increase_brightness(img):
    # Specify offset factor
    beta = 100
    # Convert to YCrCb color space
    ycbImage = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
    # Convert to float32
    ycbImage = np.float32(ycbImage)
    # Split the channels
    Ychannel, Cr, Cb = cv2.split(ycbImage)
    # Add offset to the Ychannel 
    Ychannel = np.clip(Ychannel + beta , 0, 255)
    # Histogram equilization (normalizes values after brightening)
    #Ychannel = cv2.equalizeHist(np.uint8(Ychannel))
    # Merge the channels and show the output
    ycbImage = cv2.merge([np.uint8(Ychannel), np.uint8(Cr), np.uint8(Cb)])
    imbright = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)
    cv2.namedWindow("Bright music", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Bright music", imbright)
    cv2.waitKey(0)
    return imbright

def threshold(img):
     img=1
    

def kmeans(img):    

    oneDdata = imbright.reshape((-1,3))
    oneDdata = np.float32(oneDdata)
    ##cv2.kmeans(data, K, critera, attempts)
    
    # Define criteria = ( type, max_iter = 100 , epsilon = 1.0 )
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1.0)

    # set cluster number
    k=2
    
    #apply kmeans
    compactness, label, center=cv2.kmeans(oneDdata, k, None, criteria, 2, cv2.KMEANS_RANDOM_CENTERS)
    
    #convert back data
    center = np.uint8(center)
    res = center[label.flatten()]
    kmeansIm = res.reshape((imbright.shape))
    cv2.imshow('kmeansIm',kmeansIm)
    cv2.waitKey(0)
    returns kmeansIm


def  main():
    #parsing and input from computer vision for faces module 2 brightness.py
   
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--filename")
    args = vars(ap.parse_args())

    filename = "./image_test.jpg"
    if args['filename']:
      filename = args['filename']

    img = cv2.imread(filename)
## Dialate
  
## Gaussian blur
    
## Brightness to get rid of some grey spots
#Threshold to black and white

## Kmeans to figure out average between clusters (threshold value)


def testcode():
    infile=raw_input()
    im0=Image.open(infile)
    im1=im0.convert("1") ## converts to black and white - no greyscale
    im = im1.convert("L") ## data easier to work with in this form
    im.save("black_white2.bmp")
    imageW=im.size[0] #width of music in pixels
    imageH=im.size[1] #height of music in pixels 
    im_arr = np.asarray(im) ## convert im to array
    im_arr.setflags(write=1) ## make im_arr writable

    ## save array
    np.save("convert2.npy", im_arr)
    start_time = time.time()
    obj_list1 = ssb.sep_black(im_arr, imageW, imageH)
    print "spiral sep took ", time.time()-start_time , " seconds"
    print "length of obj_list is ", len(obj_list1)
    mod_obj = ml.process_objs(obj_list1, imageW, imageH) ## list of feature dictionaries for each object
    ##print out every sorted object 
    #i = 0
    #while i < len(mod_obj):
    #    print_im(mod_obj[i]["array"], str(i))
    #    i += 1
    
    ## pickle mod_obj
    save_obj(mod_obj, "raw_obj_with_features")
    checked_obj = load_obj("raw_obj_with_features")
    i = 0
    while i < len(checked_obj):
        print mod_obj[i]["width"]
        i += 1
 
    

## given list of objects, plots  
def replot(imageW, imageH, obj_list):
    new_plot = np.zeros((imageH+1, imageW+1))
    for x in range(0, imageW+1):
        for y in range(0, imageH+1):
            new_plot[y][x] = 255
    for el in obj_list:
        for cor in el:
            new_plot[cor[0]][cor[1]] = 0
    g = np.asarray(dtype=np.dtype('uint8'), a = new_plot)
    i = Image.fromarray(g, mode = 'L')
    i.save('replot.png')

## given single object, plots
def print_im(arr, name):
    g = np.asarray(dtype=np.dtype('uint8'), a = arr)
    i = Image.fromarray(g, mode = 'L')
    i.save(name+".png")

## pickles object in file (each object + characteristics)
def save_obj(obj, filename):
    with open(filename+".pkl", 'wb') as f:
        cpickle.dump(obj, f, cpickle.HIGHEST_PROTOCOL)

## reads back object from pickled file
def load_obj(filename):
    with open(filename+".pkl", 'rb') as f:
        return cpickle.load(f)


def speedcheck(im_arr, imageW, imageH):
    lista = []
    for threadcount in range(1, 10000, 100):
        start_time = time.time()
        sb.process_whole_image(im_arr, imageW, imageH, threadcount)
        tot_time = time.time()-start_time
        lista.append(tot_time)
        print "total time for ", threadcount, " was ", tot_time

    print lista
    return lista

main()

