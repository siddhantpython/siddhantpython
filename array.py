from array import *
val=array('i',[2,3,4,-5,7])
print(val)
print(val.buffer_info())
print(val.typecode)
val.reverse()
print(val)
for i in range(len(val)):
    print(val[i])
newArr=array(val.typecode,(a*a for a in val))
for e in newArr:
        print(e)