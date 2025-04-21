

x = list(int,input().split())
def repow(c):
    if c > 0:
        return repow(c-1)
    return c
print(repow(x))
