#Takes in a pickled file of systems and clusters each system to get location of staff lines
#RUN WITH PYTHON3
#generated with horizontal runs processed from gamera_getCC.py
#info on kmeans algorithm implementation: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

from sklearn.cluster import KMeans
import sys
import pickle
import numpy as np

def main():
    #load pickled systems
    with open("systems.pkl", "rb") as f:
        systemList = pickle.load(f)
    
    line_locations=[]
    for system in systemList:
        staffs2D = system['staffs2D']
        staffs1D = system['staffs1D']

        #pick one method
        line_locations.append(gradientloc(staffs1D))        



def gradientloc(staffs1D):
    #enumerate staffs1D and delete areas where there is no data 
    #another strategy is taking second derivative...look into
    staff_gradient=np.diff(staffs1D)
    staff_gradient=list(staff_gradient)
    staff_features = []
    i=0
    while i< len(staff_gradient):
        staff_features.append([i, staff_gradient[i]])
        i+=1
    #sort by gradient value
    sort_gradient = sorted(staff_features, key=lambda tup: tup[1])
    #highest gradients should correspond to biggest jumps; i.e. beginning of line
    lines = sort_gradient[len(sort_gradient)-5 :len(sort_gradient)]
    #convert to array to slice x values
    linelocs= np.array(lines)[:,0]
    print(linelocs)
    #sort 
    return sorted(linelocs)

 
def kmeansloc(staffs2D):
    reduced_data=[]
######TRY WITH LAMBDA
#    makeNaN = lambda val: np.nan if val==0 else val
#    makeNaN(staffs2D)
#####TRY WITH FOR LOOP    
#    for rows in staffs2D:
#        for cols in rows:
#            if staffs2D[cols, rows] ==0:
#                staffs2D[cols, rows] = np.nan

    for (x,y), value in np.ndenumerate(staffs2D):
        if value != 0:
            reduced_data.append([x,y])



    reduced_data=np.asarray(reduced_data)

    kmeans = KMeans(n_clusters=5).fit(reduced_data)
    line_locations.append(kmeans.cluster_centers_)
    print("dimensions of system are "+str(len(system['staffs1D']))+" "+str(len(staffs2D[0])))
    print( kmeans.cluster_centers_)
    print (system['staffs1D'])
    print("---------")


main()
