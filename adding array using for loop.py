from numpy import *
arr1=array([1,2,3])
arr2=array([4,5,6])
arr3=([])
k=0
for i in arr1:      #code to add two arrays using for loop
    num=i+arr2[k]
    arr3.append(num)
    k+=1
print(arr3)


