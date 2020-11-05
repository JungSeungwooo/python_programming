import random

num = random.randrange(0, 10+1)
_min = 0
_max = 10
count = 0
while True:
    you = int(input(str(_min)+'~'+str(_max)+'숫자 맞추기: '))
    count += 1
    if num == you:
        print(str(count)+'번째에 맞았다')
        break
    elif num < you:
        _max = you-1
        print('더 작은 숫자로!')
    else:
         _min = you+1
         print('더 큰 숫자로!')
