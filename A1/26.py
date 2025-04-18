
d = {'even':0,'odd':0}
for i in range(3):
    if int(input())%2 == 0:
        d['even'] += 1
    else:
        d['odd'] += 1
even = d['even']
odd = d['odd']
print(f'even {even}\nodd {odd}')