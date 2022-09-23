class topten:
    def __init__(self):
        self.num=1

    def __iter__(self):  #__iter__ is function which iterates the values
        return self

    def __next__(self): #__next__ is also an inbuilt func to print the iterated value one by one
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration #stop iteration is inbuilt func  to to stop iteration from loops

values=topten()
print(next(values)) #by this print method we can print only one values at the time
for i in values:
    print(i)
