from itertools import takewhile
x = [int(input()) for _ in range(int(input()))]
x.sort()

bowls = [[0]]
# for i in x:
#     for j in range(0,len(bowls)):
#         if i > bowls[j][::-1][0]:
#             bowls[j].append(i)
#             break
#     else:
#         bowls.append([i])

# [[bowls[j].append(i) if i > bowls[j][::-1][0] else bowls.append([i]) for j in range(0,len(bowls))] for i in x]
[[] for i in x]

print(bowls)