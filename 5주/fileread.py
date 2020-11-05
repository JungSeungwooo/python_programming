
f = open('text.txt', 'r')

while True:
    line = f.readline()
    if not line: #len(line)==0
        break
    print(line, end='')
    
f.close()