def fac(x:int):
    if x ==1 or x == 0:
        return 1
    else:
        return x * fac(x-1)
print(fac(int(input())))