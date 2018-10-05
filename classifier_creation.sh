#!/bin/sh

#workflow for creating a classifier with opencv applications
# process from:
#   https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html
on_ctrl_c(){
             echo "Ignoring Ctrl-C"
         }

read -p "Annotate positive samples? Press Y or N" response1

if [ "$response1" == "Y" ] ; then

    ##### annotate positive samples
    echo -n "Enter folder path"
    read folder
    echo -n "Enter file for annotations, (must be created beforehand)" 
    read newfile


    echo -n "Running application 'opencv_annotation', for usage of annotation go \
             to https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html"
    opencv_annotation --annotations=$newfile \
                      --images=$folder

    echo -n "opencv_annotation finished"
fi

##### create positive samples
echo -n "Preparing to create positive samples. Continue? Press Y or N"
read response2

if [ "$response2" = "Y" ] ; then 

    echo -n "enter path of output file that will contain  positive samples for training"
    read vec_file_path

    echo -n "enter the name of the txt file used to specifify input images"
    read collection_file_path

    echo -n "enter the number of samples to be created- this is sum of first values per line"
    read number

    SAMPLE_WIDTH=12
    SAMPLE_HEIGHT=36

    echo -n "default width and height have been set to 12 and 36 pixels"



    opencv_createsamples -vec $vec_file_path \
                         -info $collection_file_path \
                         -num $number \
                         -show \
                         -w "$SAMPLE_WIDTH"  -h "$SAMPLE_HEIGHT"

fi

#### create classifier

echo -n "enter name path of folder where training classifier should be stored"
read folder_path

echo -n "enter path of file with annotated samples created by opencv_createsamples"
read training_set

echo -n "enter path of file listing background images"
read background_file

#defining certain variables now, can get rid of later
FOLDER_PATH="./classifiers"
TRAINING_SET="./data/flats/positive_samples.txt"
BACKGROUND_FILE="./data/flats/negative_samples.txt"


NUM_POS=30 #number of positive samples to use at every stage
NUM_NEG=45 #number of negative samples to use at every stage
NUM_STAGES=5 #number of stages to train the classifier (overriden by acceptanceRatioBreakValue?)
VAL_BUF_SIZE=2048 #Size of buffer for precalculated feature values (in Mb)
IDX_BUF_SIZE=2048 #Size of buffer for precalculated feature indices (in Mb)

## val_buf_size + idx_buf_size cannot exceed system memory

THREADS=4 #number of threads
BREAK_VALUE=.000001 #How precise your model should keep learning and when to stop. Reccomend 10e-5, to ensure the model does not overtrain on your training data

MIN_HIT_RATE=.1 #example given in viola paper
MAX_FALSE_ALARM_RATE=.3
WEIGHT_TRIM_RATE=.95 #recommended by classifier tutorial
MAX_DEPTH=1 #recommended by classifier tutorial
#MAX_WEAK_COUNT=30  #max number of trees, as many as this number to get false_alarm_rate
MODE="ALL"
FEATURE="LBP" #haar is default
opencv_traincascade -data "$FOLDER_PATH"  \
                    -vec "$TRAINING_SET" \
                    -bg "$BACKGROUND_FILE" \
                    -num_pos "$NUM_POS" \
                    -num_neg "$NUM_NEG" \
                    -numStages "$NUM_STAGES" \
                    -precalcValBufSize "$VAL_BUF_SIZE" \
                    -precalcInxBufSize "$IDX_BUF_SIZE" \
                    -numThreads "$THREADS" \
                    -acceptanceRatioBreakValue "$BREAK_VALUE" \
                    -w 12 \
                    -h 36 \
                    -minHitRate "$MIN_HIT_RATE"\
                    -maxFalseAlarmRate "$MAX_FALSE_ALARM_RATE"\
                    -weightTrimRate "$WEIGHT_TRIM_RATE" \
                    -maxDepth "$MAX_DEPTH" \
                    -maxWeakCount "$MAX_WEAK_COUNT" \
                    -mode "$MODE"


