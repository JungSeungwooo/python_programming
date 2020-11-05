f = open('text.txt', 'a')
for i in range(11,16):
    f.write('%d번째 줄\n' %(i))
f.close()
