Program Running Order:
### indicates item is complete

1. Capture Image
    a. correctDimensions.py ### gui-based
    #### works as intended but hard to specify point location in HighGUI 
    
    b. unrotate_music.py  ###
    c. scale_image.py ###  scales image to allow reasonable processing speed
2. Clean Image
    a. convert.py
    b. clean_image.sh (faster) ### uses imagemajik to clean image
    C. full_clean_image.sh ### composite that includes scaling, cleaning, and staff removal
3a. Remove staff lines
    a. gameraStaffRemoval.py ### removes staff lines from image

3b. Identify staff line location
    a. gameraStaffLocator.py (ongoing, need normalized image or dilation)

4a. Identify accidentals
    a. gamera_classifier.py #nearest neighbor, gamera
        1. classifiers
            1. knn_glyphs.xml ### training file, can keep adding. CURRENTLY BASED OFF HINDEMITH 3
            2.knnFullSymbolGlyphs.xml   
                a. from :
                    - clar_hindemith-symphony-bflat3.png
                    - louffler_vla2_no_staff
                    - strauss_no_staff.png
                    - louffler_score11.png
                    - maslanka_tears_2.png 
    b. svm (pixel)
    c. cascade (pixel)
    d. nearest neighbor- haar feature
        1. C++ plugin in gamera directory #XXXX very complicated
        2. haar.py #python plugin
        3. gamera_classifier2.py 
            a. ### Uses gamera k-nearest neighbor for size determination then applies haar nearest neighbor thru opencv 
            b. #TODO get this to work    
    e. svm (harr-feature)
    d. classifier_creation.sh  #opencv cascade classifier based on haar features
        1. #can't get it to work + need to clean positive set
        2. #folders: ./data/flats
    f. YOLO : https://www.learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/?ck_subscriber_id=272181659
    g. mask R-CNN: find actual object using deep learning
        https://www.learnopencv.com/deep-learning-based-object-detection-and-instance-segmentation-using-mask-r-cnn-in-opencv-python-c/?ck_subscriber_id=272181659
        
4b. Move staff lines according to transposition

5a. Identify Note Name
    a. location based guess
    b. nearest neighbors to staff location examples

6. Lookup table for shift

7a. Erase old accidental and print new one

7b. Erase old key signature and print new one. 
   





Proof for why only accidentals need to change

1. Defining base situation

a. Every note can be represented as (location, degree, frequency) where
            
        location -> location on staff
            location = {C, D, E, F, G, A, B}

        degree -> numerical representation within Western 12-tone scale,
            degree = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

        frequency -> frequency in hz of note that we hear. For this 
        excercise the size of the set will equal 12, corresponding to 
        1 octave
            frequency = {c, csharp, d, dsharp, e, f, fsharp,  g, gsharp
                         a, asharp,  b}
   
b.  Western music is based off an ordered set of notes of size 12, which
    will henceforth be refered to as FULL. 

  
c.  Only 7 out of the 12 members of the set have a coordinate for location. 

    These members are:  

        location of  member l(x):C    D    E     F     G    A      B        
        degree of member d(x):   1    3    5     6     8    10     12
        frequency of member f(x):c    d    e     f     g    a       b


******This subset of FULL will be refered to as visualizable subset (V)****


d.  V_location is used as an alphabet to create strings 
    To represent other members of FULL within a string, one can apply 
    local operators (preoperators) to the locations in V. 
    The operators can be:
   
      <sharp>,   where <sharp>(x) -> 
            d(x) = x+1 and f(x) = frequency shifted to the right

      <flat>, where <flat>(x) ->
            d(x) = x-1 and f(x) = frequency shifted to the left

      <natural>, where <natural>(x) ->
            d(x) and f(x) are the degree and frequency specified in V

*******This set of local operators will be refered to as O*******


    Thus a music string consists of a list of locations and operators
 

e.  In addition, global operators can also be applied to the entire 
    string (aka key signature) 
    
        Global operator are defined: 
        
             op_key(s),  where op /in O, key /in V_location, and s is a string
        
        ->  op will be applied locally to every element of key in s


    To be a valid global operator, key is constrained in that 
    if every member of key's degree shifts to its post-operated value,
    the degrees in the set consisting of (key + (V - key)) will still map
    to FULL via addition or subtraction

    For example:   
            
            If key = {B, E} and op = <flat>, the degree of B and E 
            (defined as B=12 and E=5 in FULL) would now shift to

            B = <flat>B = B-1 = 12-1 = 11
            E = <flat>E = E-1 = 5-1 = 4

            The set Q consisting of key + (V-key) would thus contain the 
            elements {<flat>B, <flat>E } + {C, D, F, G, A}, 
            which corresponds to values of  {10, 4} + {1, 3, 6, 8, 10}

            Ordering the values in N, you get 
                {1, 3, 4, 6, 8, 10, 11}
            Adding 2 to each value gives you 
                {1+2, 3+2, 4+2, 6+2, 8+2, 10+2, 11+2}

               ={3,   5,   6,   8,   10,  12,   1} = FULL 
                (Remember 13mod12 is 1) 

            Thus since N maps to FULL, <flat>_{B,E} is a valid global 
            operation. (in musical terms, this is the key of B flat and 
            is represented by the Bflat key signature)


2.Proof

a. Define Transposition
    
    A Transposition is a function that takes a set of notes and shifts the frequency while 
    keeping location and degree constant

    For example: 
        TRANSPOSITION_n(FULL) where n /in frequency defines a new set T where 
            (L, D, F) -> (L, D, F+(n-c)), where L= location, D = degree, F= frequency 
            and c is the constant frequency detail in 1a   
       

b.  Posit: If  TRANSPOSITION_n were applied onto a music string, the string would 
    retain the same length and retain the same position of local operations; 
    no new local operations would need to be added 
    






