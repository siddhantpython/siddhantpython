from array import *
val=array('i',[5,6,7,2,8,1])
print("elements in original array:")
for i in range(0,len(val)):
    print(val[i],end=" ")
#now sorting array in ascending order
for i in range(0,len(val)):
    for j in range(i+1,len(val)):
        if (val[i]>val[j]):
            temp=val[i]
            val[i]=val[j]
            val[j]=temp
print()
#displaying all elemnets of arraay in ascending order
print("elment of array in ascending order:")
for i in range(0,len(val)):
    print(val[i],end=" ")