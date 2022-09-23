class computer:
    def __init__(self, rama, cpun, roma):
        self.ram = rama
        self.cpu = cpun
        self.rom = roma


    def config(self):
        print('config is ;', self.ram, self.cpu, self.rom)


comp1 = computer(18,'i7','1tb')     #creating object comp1 and comp2
comp2 = computer(8,'i8','200gb')

#comp1.config()
#omp2.config()


class identity:
    def __init__(self):
        self.name='siddhant'
        self.age=22
    def details(self):
        print('name is :',self.name)
        print('age is:',self.age)
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1=identity()
c2=identity()

c1.details()
c2.age=25 #by this parameter we can change the values of object
c2.details()

if c1.compare(c2):
    print('the age is same')
else:
    print('the age is different')


# class variables and instance variables:

class car:
    wheels=4  #wheel is class variable.  all variables above __init__ function are class variables

    def __init__(self):
        self.mileage=10    #mileage and company are instance variables.   all variables under __init__ function are instance variable
        self.company="BMW"

a1=car()
a2=car()
print(a1.mileage,a1.company,car.wheels)
print(a2.mileage,a2.company,car.wheels)
# class variables are common variables i.e., if we change it , it get chAnge for all objects

a1.mileage= 8 #we access the instance variables through objects we created
car.wheels= 3 #we access the class variables through the class name in which it is created
print(a1.mileage,a1.company,car.wheels)
print(a2.mileage,a2.company,car.wheels)