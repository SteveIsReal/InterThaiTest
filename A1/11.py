x = ' '.join(input().upper()).split(' ')
c = dict()
b = list()
for i in x:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
for i,v in c.items():
    b.append(str(v))
    b.append(i)
print(''.join(b))

