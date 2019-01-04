#from create annotations, get pngs of all the trial data
import cv2
import str


def main():

    #read in opencv annotation file
    filepath = "./data/flats/raw_positive_samples.txt"

    with open(filepath, "r") as f:

        for line in f:
            l1=0                          #line number, used in naming
            str.split(line)              #get tokens

            music_path_end = line[0]     #file annotations are taken from
            music_path = "./data/flats/"+music_path_end

            #open music file to begin splicing
            music_file = cv2.imread(music_path)

            num_samples = line[1]        #number of samples in line, check to match

            index = 2
            l2=1                         #line number, used in naming
            while index < len(line):
                coor = line[index : index + 4]
                training_im = music_file[coor[0]:coor[1], coor[2]:coor[3]]
                cv2.imwrite("data/flats/trainingImageFolder/image"+str(l1)+"-"+str(l2), \
                        training_im)
                index+=4
                l2+=1

            l1+=1




