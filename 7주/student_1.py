class Student:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print('생성됨')
        
    def __del__(self):
        print('소멸됨')
    
    def __add__(self, other):
        print('더해짐')
        return Student(self.name + ' ' + other.name, self.age+other.age)

    

if __name__ == '__main__':
    l1 = dir(Student)
    print(l1)