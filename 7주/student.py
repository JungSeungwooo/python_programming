class Student:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    

if __name__ == '__main__':
    l1 = dir(Student)
    print(l1)