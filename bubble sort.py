#prog for sorting list in ascending order using bubble sort:
#in this we compare 2 values per iteration

def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
               #swapping the values if "if" condition is satisfied
               if nums[j]>nums[j+1]:
                   temp=nums[j]
                   nums[j]=nums[j+1]
                   nums[j+1]=temp
               #print(nums)

nums=[5,6,3,7,8,2]

bubble_sort(nums)
print(nums)

#program for sorting using "selection sort":in this method we swap only once in outer loop,here we assume the min value with index no. (0)
#then we compare the min value with all other values in list and arrange accordingly

def selection_sort(list):
    for i in range(len(list)):
        minpos=i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j

        temps=list[i]
        list[i]=list[minpos]
        list[minpos]=temps
       # print(list)


list=[5,3,6,7,8,9,4,2]

selection_sort(list)
print(list)