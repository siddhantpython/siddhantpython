from abc import ABC,abstractmethod    #abc:absract base classes
#python does not support abstract class hence we import module "abc"
class computer:             #abstract classes is class in which we have only method definition no body.
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("it's running")

class programmer(computer):
    def work(self,com):
        print("solving bugs")
        com.process()

class whiteboard:
    def write(self):
        print("writing")


com=computer()
lap=laptop()
prog=programmer()
wht=whiteboard()
prog.work(lap)
wht.write()