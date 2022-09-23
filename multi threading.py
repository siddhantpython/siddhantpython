from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hii(Thread):
    def run(self):
        for i in range(5):
            print("hiii")
            sleep(1)

a1=hello()
a2=hii()

a1.start()
sleep(0.5)
a2.start()
a1.join()
a2.join()
print("multithreading executed succesfully")