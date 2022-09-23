def count(lst):
    even=0
    odd=0
    for i in lst:
        if i %2==0:
            even+=1
        else:
            odd+=1
    return even, odd
lst=[2,4,3,6,7,5,24,20,11,12,13,8]

even, odd=count(lst)

#printing no. of names with more than 5 letters:

print("even: {} and odd: {}".format(even,odd))
def nam(name):
    more=0
    for i in name:
        if len(i)>5:
            print(i)
            more+=1
    return more
name=['sidd','aman','harsh','aarohi','anjali','atharva','gaurav','virat']
more=nam(name)
print('name with more than 5 letters: {}'.format(more))


