def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    if n==1:
        print(a)
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(5)
#code for factorial of the number:
def fact(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    return f
x=int(input("enter x:"))
result=fact(x)
print("factorial of x is:", result)


