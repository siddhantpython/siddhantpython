a,b=10,0
try:#try block will try to run prog if found error it will jump to except block

    print("resource open")
    k=int(input("enter the value: "))
    print(a/b)
except ZeroDivisionError as e:#except blick will run only when there is error in try block
    print("can't divide number by zero")

except ValueError as e:
    print("invalid input")

except Exception as e:#exception will run only when ther is some error which we don't know
    print("something went wrong")

finally:#finally block is that block which will always run no matter there is error or not
    print("resource closed")