#in operator overloading all the inbuilt functions like add, multiply, sub are overide or changed according to requirement by user

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other): # __add__inbuilt function to add to values
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self, other):  #__gt__ is a inbuilt function to compare
        b1=self.m1+self.m2
        b2=other.m2+other.m2
        if b1>b2:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.m1,self.m2)

s1=student(50,45)
s2=student(40,40)
s3=s1+s2
print(s3.m1)
print(s3.m2)
if s1>s2:
    print('s1 is greater')
else:
    print('s2 is greater')
print(s1)
print(s2)