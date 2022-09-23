#linear search in python
#pos=0

#def search(list,n):
 #   for i in list:
  #      if list[i]==n:
        #    globals()['pos']=i
   #         return True
    #    else:
     #       return False
#list=[1,2,3,4,6,5,7,9]
#n=int(input('enter the value to search '))
#if search(list,n):
 #   print("found at :",pos+1)

#else:
 #   print('not found')




#Binary search in python :

loc=-1
def search(list,n):
    l=0   #l is lower bound
    u=len(list)-1 #u is upper bound
    while l <= u:
        mid = (l+u) // 2 #we found the mid point of lower and upper bound
        if list[mid] == n:
            globals()['loc']=mid
            return True
        else:
            if list[mid]<n: #if value to be searched is greater than mid value then we change the mid value we founded into lower bound value
                l=mid+1
            else:
                u=mid-1 #if value to be found is less than mid value then we change the upper bound value to mid value
    return False


list = [4,5,6,7,8,88,99,76,65,77,45,67,245,76478,86457]
list.sort() #binary search always execute in sorted list hence before calling for search we should sort the list
print(list)
n=89
if search(list,n):
    print("found at:",loc+1)

else:
    print("not found")
















