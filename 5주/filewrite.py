
f = open('text.txt', 'w')
for i in range(1,11):
    f.write('%d번째 줄\n' %(i))
f.close()

