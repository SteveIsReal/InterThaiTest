x = []
for i in range(3):
    x.append(int(input()))
if x[0] < x[1] < x[2]:
    print('increasing')
elif x[0] > x[1] > x[2]:
    print('decreasing')
else:
    print('neither')
