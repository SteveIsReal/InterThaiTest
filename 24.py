y,c = int(input()), int(input())
k,v = '',''
rate = {
    'less 1500':[250,100,0],
    '1500-2000':[400,300,200],
    'more 2000':[1000,700,500]
}
if c <= 1500:
    k = 'less 1500'
elif c > 1500 and c <= 2000:
    k = '1500-2000'
elif c > 2000:
    k = 'more 2000'

if y <= 1990:
    v = 0
elif y >= 1991 and y <= 1999:
    v = 1
elif y >= 2000:
    v = 2
print(rate[k][v]+1000)