#various methods: instance method, class method , static method

class student:
    school="Telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def get_school(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is student class")
s1=student(12,24,36)
s2 =student(8,16,24)
print(s1.m1,s1.m2,s1.m3)
print(s2.m1,s2.m2,s2.m3)

print(s1.avg())
print(s2.avg())

print(student.get_school())
student.info()