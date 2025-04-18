# season = ['winter','spring','summer','fall']
# m = int(input())
# d = int(input())
# inx = int()
# if m >= 1 and m <=3:
#     inx = 0
# elif m >= 4 and m <=6:
#     inx = 1
# elif m >= 7 and m <=9:
#     inx = 2
# elif m >= 10 and m <=12:
#     inx = 3

# if m %3 == 0 and d >= 21:
#     inx = inx+1 if inx < 3 else 0
# print(season[inx])

season = ['winter','spring','summer','fall']
nonth = [[j*3+i+1 for i in range(3)] for j in range(4)]
print(nonth)