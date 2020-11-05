import random

num = random.randrange(0, 10+1)
count = 0
while True:
    you = int(input('0~10 숫자 맞추기: '))
    count += 1
    if num == you:
        print(str(count)+'번째에 맞았다')
        break
