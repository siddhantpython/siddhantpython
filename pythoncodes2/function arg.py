def person(name,age):
    print(name)
    print('age:', age)
person(age=22,name='sid')

def sum(a, *b):# *b means b can have multiple values
    c=a
    for i in  b:
        c=c+i
        print(c)
sum(5,4,1,5,10)

def individual(name, **data): # ** means data can have multiple values with keywords
    print(name)
    print(data)
individual('sid',age=22,city='dehradun', mobno=8954138600)
#or we can also do by using for loop:
def who(name,**data):
    print(name)
    for i,j in data.items():# .items() is inbuilt function
        print(i,j)
who('sid', age=22, city='dehradun',phone=8954138600)