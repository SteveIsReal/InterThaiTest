
x = list()
for i in range(int(input())):
    x.append(int(input()))
x.sort()

bowls = [[0]]
for i in x:
    for j in range(0,len(bowls)):
        if i > bowls[j][::-1][0]:
            bowls[j].append(i)
            break
    else:
        bowls.append([i])

print(len(bowls))