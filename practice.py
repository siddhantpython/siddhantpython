def fib(n):
    a,b=0,1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            if c<100:
               print(c)
               a=b
               b=c

## filter reduce map functions:
#from functools import reduce
#a=[2,4,5,6,8,3,10]
#evens =list(filter(lambda n:n%2==0, a))  #lambda is an anonymous function
#print(evens)
#double=list(map(lambda n: n*2,evens))
#print(double)
#sum=reduce(lambda x,y:x+y,double)
#print(sum)

#decorators:
def sub(a,b):
    print(a-b)


def smart_sub(func):   #this is decorator
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner
sub=smart_sub(sub)

sub(2,5)








