x,y = input(), input()
z = x[::-1]
if y == "+":
    c = int(x)+int(z)
    print(f'{int(x)} + {int(z)} = {c}')
elif y == "*":
    c = int(x)*int(z)
    print(f'{int(x)} * {int(z)} = {c}')