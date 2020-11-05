class Student:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def hello(self):
        print("Hi, my name is %s." % self.name)
    def myage(self):
        print("My age is %d." % self.age)
        
    
if __name__ =='__main__':
    s1 = Student('Adam', 20)
    s2 = Student('Smith', 21)
    s1.hello()
    s2.hello()
    s1.myage()
    s2.hello()
    s2.myage()