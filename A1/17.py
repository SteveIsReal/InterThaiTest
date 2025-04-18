y1,m1,d1 = int(input()),int(input()),int(input())
y2,m2,d2 = int(input()),int(input()),int(input())

y3,m3,d3 = (y1 - y2),(m1-m2),(d1-d2)

value = 0

if y1 < y2:
    value = 1
elif y2 < y1:
    value = 2
elif y2 == y1:
    if m1 < m2:
        value = 1
    elif m2 < m1:
        value = 2
    elif m2 == m1:
        if d1 < d2:
            value = 1
        elif d2 < d1:
            value = 2
        elif d1 == d2:
            value = 0
print(value)