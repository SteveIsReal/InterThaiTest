x = int(input())
def re(x):
    if x == 1 or x == 0:
        return x
    else:
        return x ** 2 + re(x-1)
print(re(x))