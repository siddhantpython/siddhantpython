a=10              #this "a" is global variable
def here():
    global a      #global word is used to change value of "a" outside function
    a=15          #this 'a' is local variable
    print('inside function:', a)
here()
print('outside a:', a)
#when we have multiple global values and we want global and local in same function then we use fun globals():

b=10
print(id(b))
def now():
    b=5
    x=globals()['b']
    print(id(x))
    print('in fun b;', b)
    globals()['b']=15

now()
print('out b;',b)
#above we can see we have both global and local variable in same function