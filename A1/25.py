jqk = ['ace','jack','queen','king','spades','clubs','diamonds','hearts']
x = input().upper()
v = ' '.join(x).split(' ') if len(x) == 2 else [x[:2],x[2]]
print(f'{v[0] if v[0].isnumeric() else [i for i in jqk if i[0].upper() == v[0]][0]} of '
      f'{[i for i in jqk if i[0].upper() == v[1]][0]}')