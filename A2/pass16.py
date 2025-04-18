x,y = input().split(), input().split()
v = True if x[0] is y[0] else False
g = 1000 if v else 100
if x[1] == y[1]:
    if v:
        print(1_000_000)
    else:
        print(100_000)
elif x[1][2:] == y[1][2:]:
    print(2*g)
elif x[1][3:] == y[1][3:]:
    print(g)
elif v:
    print(20)
else:
    print(0)
