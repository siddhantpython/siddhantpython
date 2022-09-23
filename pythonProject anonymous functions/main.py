#anonymous function are those which are without name
#these are denoted by lambda

from functools import reduce
nums=[2,3,4,5,6,7,8,9]
even=list(filter(lambda a:a%2==0,nums))   #filter func. filters out the certain values from list acc. to our command
print(even)
doubles=list(map(lambda a:a*2,even)) #map function helps to perform certain operations in list through function
print(doubles)
sum=reduce(lambda a,b:a+b,doubles) #reduce function always takes 2 values at a time
print(sum)