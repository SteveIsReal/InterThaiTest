x = int(input())
c = ''
for i in range(x,-1,-1):
    if i % 10 == 0:
        c += f'{i} '
print(c)