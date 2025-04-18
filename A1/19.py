x = list()
for i in range(3):
    x.append(int(input()))
x = set(x)
if len(x) == 1:
    print('all the same')
elif len(x) == 3:
    print('all different')
else:
    print('neither')