x,y = int(input()), input()
if y.upper() == 'C':
    print('solid' if x <= 0 else 'liquid' if x<100 else 'gas')
elif y.upper() == 'F':
    print('solid' if x <= 32 else 'liquid' if x < 212 else 'gas')