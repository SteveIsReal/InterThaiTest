x = int(input())
v = (input().split())[:x]
c = list(map(int, v))
bird_stand = 0
for i in range(0,len(c)):
    if i == 0:
        if c[i] > c[i+1]:
            bird_stand += 1

    elif i == (len(c)-1):
        if c[i-1] < c[i]:
            bird_stand += 1

    else:
        if c[i-1] < c[i] > c[i+1]:
            bird_stand += 1

print(bird_stand)