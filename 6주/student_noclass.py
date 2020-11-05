names = []
ages = []

def AddStudent(name, age):
    names.append(name)
    ages.append(age)
    
AddStudent(' Adam', 20)
AddStudent(' Smith', 21)

print('총 학생 수= ', len(names))
for i in range(len(names)):
    print('Hi, my name is', names[i])
    print('My age is', ages[i])
