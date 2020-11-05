import random
import sys

num = random.randrange(17, 81+1)
_min = 17
_max = 81
count = 0
flag = True
while count <5:
    you = int(input(str(_min)+'~'+str(_max) +'숫자 맞추기: '))
    count += 1
    if num == you: 
        print('성공' + str(count) + '번째에 맞았다')
        flag = flase
        break
    elif num < you:
        _max = you-1
        print('더 작은 숫자로!')
    else:
         _min = you+1
         print('더 큰 숫자로!')


if flag:
    print('틀렸다! 나의 숫자는: ' + str(num))
    sys.exit()
else:
    sys.exit()
         

