class A:
    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')
class B(A): #B is inheriting all the features of A .this is single inheritance
    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')


class C(A,B):#C is inheriting all the features of A and B.This is multiple inheritance
    def feature5(self):
        print('feature 5 is working')

    def feature6(self):
        print('feature 6 is working')

a1=A()
b1=B()
c1=C()

#By the inheritance we can use functions and features of different classses