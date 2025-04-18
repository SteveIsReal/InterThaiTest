x = list()
total = 0
for i in range(int(input())):
    x.append(input().upper())

for i in 'AEIOU':
    total+=x.count(i)
print(total)
