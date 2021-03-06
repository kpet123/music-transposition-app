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


DIA_KERNEL_DIM = (2,2) #dimension of kernel in dilate
ERODE_KERNEL_DIM = (2,2)
DILATE_ITERATIONS = 1
ERODE_ITERATIONS = 1
GAUSS_KERNEL_SIZE = (5,5)
BETA = 125 #brightness
THRESH = 10 #thresholding

sys.setrecursionlimit(50000)


## collection of different methods to apply to image to make more clear
##figure out what the variables mean
def adaptiveThreshold(img):
    size = len(img[0])/3
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
            cv2.THRESH_BINARY,size,2)
    return img


def dilate(img):
    kernel = np.ones(DIA_KERNEL_DIM, np.uint8)
    dilated_im = cv2.dilate(img, kernel, DILATE_ITERATIONS)
    cv2.imshow("dilated image", dilated_im)
#    cv2.imwrite("di.jpg", dilated_im)  
    cv2.waitKey(0)
    return dilated_im

def erode(img):
    kernel = np.ones(ERODE_KERNEL_DIM, np.uint8)
    eroded_im = cv2.erode(img, kernel, ERODE_ITERATIONS)
    cv2.imshow("eroded image", eroded_im)
#    cv2.imwrite("ero.jpg", eroded_im)  
    cv2.waitKey(0)
    return eroded_im
    
def gaussian_blur(img):
    # 5x5 kernel, (0,0) implies sigma calculated automatically
    gauss_im=cv2.GaussianBlur(img,GAUSS_KERNEL_SIZE,0,0)
    cv2.imshow("Gaussian Blur", gauss_im)
    cv2.waitKey(0)
#    cv2.imwrite("gaussian.jpg", gauss_im)
    return gauss_im

def increase_brightness(img):
    # Convert to float32
    img = np.float32(img)
    # Add offset to img 
    imbright = np.clip(img + BETA, 0, 255)
    # Histogram equilization (normalizes values after brightening)
    imbright = cv2.equalizeHist(np.uint8(imbright))
    # Merge the channels and show the output
    cv2.namedWindow("Bright music", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Bright music", imbright)
    cv2.waitKey(0)
    return imbright

def threshold(img):
    maxValue= 255
    th, thresh_im = cv2.threshold(img, 0, maxValue, \
            cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print "th is ", th
    th2, thresh_im = cv2.threshold(img, th, maxValue, \
            cv2.THRESH_BINARY)
    print "th2 is ", th2
    th3, thresh_im =  cv2.threshold(img, 2, maxValue, \
            cv2.THRESH_BINARY)

    cv2.namedWindow("thresh_im", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("thresh_im", thresh_im)
    cv2.waitKey(0)
#    cv2.imwrite("thresh.jpg", thresh_im)
    return thresh_im


   

def kmeans(img):    

    oneDdata = img.reshape((-1,3))
    oneDdata = np.float32(oneDdata)
    ##cv2.kmeans(data, K, critera, attempts)
    
    # Define criteria = ( type, max_iter = 100 , epsilon = 1.0 )
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 1.0)

    # set cluster number
    k=2
    
    #apply kmeans
    compactness, label, center=cv2.kmeans(oneDdata, k, None, criteria, 2, cv2.KMEANS_RANDOM_CENTERS)
    
    #convert back data
    center = np.uint8(center)
    res = center[label.flatten()]
    kmeansIm = res.reshape((img.shape))
    cv2.imshow('kmeansIm',kmeansIm)
    cv2.waitKey(0)
    return kmeansIm


def  main():
    #parsing and input from computer vision for faces module 2 brightness.py
   
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--filename")
    args = vars(ap.parse_args())

    filename = "./image_test.jpg"
    if args['filename']:
      filename = args['filename']

    img = cv2.imread(filename, 0)
    ##reverse
#    img = ~img
#    cv2.imshow("reversed_im", img)
#    cv2.waitKey
    #equalize
    cladh = cv2.createCLAHE()
    img = cladh.apply(img)
    cv2.imshow("clahe equalized", img)
    cv2.waitKey(0)
    img = dilate(img)
## Brightness to get rid of some grey spots
    img = increase_brightness(img)
 
    ##threshold
    img = threshold(img)
    cv2.imshow("thresholded imgae", img)
    cv2.waitKey(0)
      #Threshold to black and white
#    img = threshold(img)
    ## Dialate
    #img = dilate(img)
    cv2.imwrite("process_img.jpg", img)
    cv2.destroyAllWindows()
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

