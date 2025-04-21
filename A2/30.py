
x = []
for i in range(5):
    x.append(map(int,input().split()))
for i in x:
    print(sum(i))
    if sum(i) % 2 != 0:
        print('enter loop1')
        result = 0
        for j in i:
           result += j
           if result % 2 != 0:
               print(f'{x.index(i)} {i.index(j)}')
               break
else:
    print(-1, -1)

