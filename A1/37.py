number_format = {
    '0':'',
    '1': 'a',
    '2': 'aa',
    '3': 'aaa',
    '4': 'ab',
    '5': 'b',
    '6': 'ba',
    '7': 'baa',
    '8': 'baaa',
    '9': 'ac',
}
roman_number = [['M','D','C'],['C','D','M'],['X','L','C'],['I','V','X']]
roman_number = roman_number[::-1]
x = ' '.join(input()).split(' ')
f = []
for i in x:
    f.append(i.replace(i,number_format[i]))

new_roman = roman_number[:len(f)][::-1]

for i in range(len(f)-1,-1,-1):
    f[i] = f[i].replace('a',new_roman[i][0])
    f[i] = f[i].replace('b', new_roman[i][1])
    f[i] = f[i].replace('c', new_roman[i][2])
print(''.join(f))