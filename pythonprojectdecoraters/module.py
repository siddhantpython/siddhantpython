from calc import *  #we call the another module known as calc

a=8
b=2

c=add(a,b)
d=sub(a,b)
e=div(a,b)
#here we haven't created the add() func so we will call it from another module which is 'calc'
print (c,d,e)