x,y = input(),int(input())
correct = [0,0]
if x == 'H':
    correct[0] = 1
if y == 4567:
    correct[1] = 1

if correct == [1,1]:
    print('safe unlocked')
elif correct == [1,0]:
    print('safe locked - change digit')
elif correct == [0,1]:
    print('safe locked - change char')
else:
    print('safe locked')