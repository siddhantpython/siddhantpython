#defining and calling the function
def greet():  #defining of funtion
    print('hello')
    print('good morning')
def add(x,y): #defining other function add
    c=x+y
    print(c)
#now call the above defined function
greet()
add(5,4)
#returning of values:
def mul_sub(m,s):
    a=m*s
    b=m-s
    return a,b
result1,result2= mul_sub(4,5)
print(result1,result2)

