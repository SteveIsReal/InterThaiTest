x,c = input().lower(),0
if len(x) == 3 and x.isalpha():
    for i in x:
        if i in 'aeiou':
            c += 1
    print(c)