x = int(input())
c = [list(map(int,' '.join(input()).split())) for i in range(2)]
invaild = 0
for i in range(x):
    if c[0][i] + c[1][i] != 9:
        invaild += 1
print(f'NO {invaild}' if invaild else 'YES')
