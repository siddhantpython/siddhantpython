from numpy import *
val=array([
          [1,2,3,4,5,6],
          [4,5,6,7,8,9]

          ])
print(val)
print(val.ndim) #it print the no. of dimensions of array
print(val.shape)#it print no. of rows and columns of array
#we can make 2d array into 1d by fun. called flatten():
val1=val.flatten()
print(val1)
#to convert 1d into 3d or any shape we use reshape
val2=val1.reshape(3,4)
print(val2)
#matrix function
m=matrix('1 2 2;3 4 5;6 7 8')
print(m)
#if we want to print all diagonal element of matrix then:
print(diagonal(m))
#we can also add matrices also multiply them as:
c1=matrix('1 2 3;4 5 6;7 8 9')
c2=matrix('3 2 1;6 5 4;9 8 7')
c3=c1*c2
print(c3)