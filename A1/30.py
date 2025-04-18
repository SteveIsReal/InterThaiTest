n,v = int(input()),input().split()
b = list()
for i in range(1,len(v)+1):
    if i%2 == 0:
        b.append(v[i-2:i])
x = list()
for i in b:
    x.append([int(i[0]),int(i[1])])
v = list()
text = ''
for i in x:
    v.append(max(i))
if len(v) > 1:
    print(' + '.join([str(i) for i in v]),'=',sum(v))
elif len(v) == 1:
    print(v[0])
