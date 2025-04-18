x = int(input())
c = []
for i in range(x):
    c.append([int(i) for i in input().split()])

max_value = max([max(i) for i in c])