f = open('text.txt', 'a')
while True:
    name = input('이름: ');
    if len(name) ==0: # if not name:
        break
    id = input('학번: ');
    score = int(input('점수: '));
    f.write('%s %s %d\n' % (name, id, score))
    
f.close()