from itertools import cycle

v = ['Red','Green','Blue']
p = input().split()
x = cycle(v if p[0].upper() == 'R' else [v[1],v[2],v[0]] if p[0].upper() == 'G' else [v[2],v[0],v[1]])
z = [next(x) for i in range(int(p[1]))]
print(*z, sep=" ")
