
x = [input().split() for _ in range(int(input()))]
v = [] 
for i in x:
    [v.append(i) if int(i[1]) > 15 else None]

[print(len(v)) if len(v) > 0 else None]
v = sorted(v,reverse=True,key=lambda c: c[1])
print(f"{' '.join(v[0])}" if len(v) > 0 else "")
