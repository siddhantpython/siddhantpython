from numpy import *
arr1=array([

           [1,2,3],
           [4,5,6]
           ])
arr2=array([
            [2,3],
            [4,5],
            [6,7]
           ])
arr3=([
    [0,0],
    [0,0]
      ])
#iterating through rows:
for i in range(len(arr1)):
    #iterating through column:
    for j in range(len(arr2[0])):
        #iterating by rows:
        for k in range(len(arr2)):
            arr3[i][j]+=arr1[i][k] * arr2[k][j]
for re in arr3:
    print(re)


