#from create annotations, get pngs of all the trial data
import cv2
import string


def main():

    #read in opencv annotation file
    filepath = "./data/flats/testfile.txt"
    print "test0"
    with open(filepath, "r") as f:

        l1=0                          #line number, used in naming
        
        for line in f:
            tokens = string.split(line)              #get tokens

            music_path_end = tokens[0]     #file annotations are taken from
            music_path = "./data/flats/"+music_path_end

            #open music file to begin splicing
            music_file = cv2.imread(music_path)

            num_samples = tokens[1]        #number of samples in line, check to match
            print "num samples is ", num_samples
            index = 2
            l2=1                         #line number, used in naming
            while index < len(tokens):
                coor = tokens[index : index + 4]
                print coor
                training_im = music_file[int(coor[1]): int(coor[1])+int(coor[3]), \
                        int(coor[0]) :int(coor[0])+int(coor[2])]
                training_im_path = "data/flats/trainingImageFolder/batch2image"+str(l1)+\
                        "-"+str(l2)+".png"
                cv2.imwrite(training_im_path, training_im)
                index+=4
                l2+=1

            l1+=1



main()
