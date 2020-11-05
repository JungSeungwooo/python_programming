class animal:
    def sound(self):
        print('...')
    
class dog(animal):
    def sound(self):
        print('멍멍')
    
class cat(animal):
    def sound(self):
        print('야옹')

l1 = []
l1.append(dog())
l1.append(cat())
for a in l1:
    a.sound()

    