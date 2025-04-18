
x = int(input())
c = {'10':0,
     '5':0,
     '2':0,
     '1':0
     }

while x >= 0:
    if x-10 >= 0:
        c['10'] += 1
        x -= 10
    elif x-5 >= 0:
        c['5'] += 1
        x -= 5
    elif x-2 >= 0:
        c['2'] += 1
        x -= 2
    elif x-1 >= 0:
        c['1'] += 1
        x -= 1
    else:
        break

for i,v in c.items():
    print(f'{i} = {v}')