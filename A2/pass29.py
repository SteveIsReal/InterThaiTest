

x = int(input())
print('0')
if x > 1:
    for i in range(2,x):
        print('0 ',end='')
        print('1 '*(i-2),end='')
        print('0')
    print('0 '*x,end="")

