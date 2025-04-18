x = []
c = [10,40,50]
for i in range(3):
    x.append(int(input()))
for i in x:
    if i < (c[x.index(i)]/2):
        print('fail')
        break
else:
    print('pass')