

x = list(map(int,input().split()))
y = []

for i in range(1,x[0]+1):
    y.append(i**2)

z = y.copy()

for i in y:
    if x[1] - i >= 0:
        x[1] -= z.pop(0)
    else:
        break
print(len(z))
    


