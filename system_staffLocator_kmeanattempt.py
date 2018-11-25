#Takes in a pickled file of systems and clusters each system to get location of staff lines
#RUN WITH PYTHON3
#generated with horizontal runs processed from gamera_getCC.py
#info on kmeans algorithm implementation: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

from sklearn.cluster import KMeans
import sys
import pickle
import numpy as np

#load pickled systems
with open("systems.pkl", "rb") as f:
    systemList = pickle.load(f)

#find centroids for staffs using staffs1D
line_locations=[]
for system in systemList:
    staffs2D = system['staffs2D']
    staffs2D = staffs2D.astype(int) 
#    makeNaN = lambda val: np.nan if val==0 else val
#    makeNaN(staffs2D)
    
    for rows in staffs2D:
        for cols in rows:
            if staffs2D[cols, rows] ==0:
                staffs2D[cols, rows] = np.nan

    print(staffs2D)
    kmeans = KMeans(n_clusters=5).fit(staffs2D)
    line_locations.append(kmeans.cluster_centers_)
    print( kmeans.cluster_centers_)


