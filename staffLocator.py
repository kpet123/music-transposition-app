#RUN WITH PYTHON3
#generated with horizontal runs processed from get_run_projection.py

import sklearn
import sys
import pickle


with open("projection.pkl", "rb") as f:
    hor_projection = pickle.load(f)


print( hor_projection)
