#Takes in a pickled file of systems and clusters each system to get location of staff lines
#RUN WITH PYTHON3
#generated with horizontal runs processed from gamera_getCC.py
#info on kmeans algorithm implementation: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

from sklearn.cluster import KMeans
import sys
import pickle
import numpy

#load pickled systems
with open("systems.pkl", "rb") as f:
    systemList = pickle.load(f)

#find centroids for staffs using staffs1D
line_locations=[]
for system in systemList:
    staffs1D = system['staffs1D']
    #enumerate staffs1D and delete areas where there is no data 
    #another strategy is taking second derivative...look into
    staff_gradient=numpy.diff(staffs1D)
    staff_features = enumerate(staffs1D)
    staff_features = diff
