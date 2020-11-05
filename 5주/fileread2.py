f = open('text.txt', 'r')
contents = f.readlines()
for const in contents:
    print(const, end='')
f.close()