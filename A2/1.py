#
# x = [10,20,30,40,50]
# f = [2,3,4,5,6]
#
# d = map(
#     lambda w,h: w*h,
#     x,
#     f
# )
# print(list(d))
'''
from itertools import cycle

s = cycle(['1','2','3'])
print(next(s))
print(next(s))
print(next(s))
print(next(s))
'''

from datetime import datetime

now = datetime.now()
print(now)
print(f'{now:%H : %M : a%S}')

x = 1
d = 2
total = x+d

print(f'{x} + {d} = {x+d}')
print(f'{x + d = }\n'
      f'{total = }')
print([[1,2],[2],[3]][0][::-1][0])