x = input().split()
y = []
for i in x:
    if i not in y:
        y.append(i)
print(' '.join(y))
