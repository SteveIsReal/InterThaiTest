x = int(input())
f = ''
for i in range(1,x+1):
    f += '*' if i%5 else 'X'
print(f)