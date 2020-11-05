f = open('text.txt', 'r')
contents = f.readlines()
f.close()

total = 0
for item in contents:   # item = 'kim 100 90\n'
    itemlist = item.split()
    score = int(itemlist[2])
    total += score
count = len(contents)
print('인원수:', count , '총점:', total, '평균: ', total/count)
