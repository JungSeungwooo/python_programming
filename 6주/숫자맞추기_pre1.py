import random

num = random.randrange(0, 10+1)
you = int(input('0~10 숫자 맞추기: '))
if num == you:
    print('맞았다')
else:
    print('틀렸다! 나의 숫자는:', num)
