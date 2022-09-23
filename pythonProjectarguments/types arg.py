def person(name,age):
    print("age is: ", age)
    print("name is :", name)
person(name='sid',age=22) #this is keyword argument

def sum(a,*b): #*b is the vaiable length arg which means we can have multiple values for b
    c=a
    for i in b:
        c=c+i
        print(c)

sum(5,10,20,30,40)

def guy(name,**data): # here double star means keyworded argument,i.e we  can have multiple keywords and their values
    print(name)
    for i ,j in data.items():
        print(i,j)

guy("sid",age=22,state="uttrakhand",mob=8954138600)