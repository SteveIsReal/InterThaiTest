d,m = int(input()), int(input())
x = {
    'capricorn': [[12,[i for i in range(22,32)]],[1,[i for i in range(1,20)]]],
    'aquarius': [[1,[i for i in range(20,32)]],[2,[i for i in range(1,19)]]],
    'pisces': [[2,[i for i in range(19,30)]],[3,[i for i in range(1,21)]]],
    'aries': [[3,[i for i in range(21,32)]],[4,[i for i in range(1,20)]]],
    'taurus': [[4,[i for i in range(20,31)]],[5,[i for i in range(1,21)]]],
    'gemini': [[5,[i for i in range(21,32)]],[6,[i for i in range(1,22)]]],
    'cancer': [[6,[i for i in range(22,31)]],[7,[i for i in range(1,23)]]],
    'leo': [[7,[i for i in range(23,32)]],[8,[i for i in range(1,23)]]],
    'virgo': [[8,[i for i in range(23,32)]],[9,[i for i in range(1,23)]]],
    'libra': [[9,[i for i in range(23,31)]],[10,[i for i in range(1,24)]]],
    'scorpio': [[10,[i for i in range(24,32)]],[11,[i for i in range(1,22)]]],
    'sagittarius': [[11,[i for i in range(22,31)]],[12,[i for i in range(1,22)]]]
}

for i,v in x.values():
    if m == i[0]:
        if d in i[1]:
            print(*[a for a,b in x.items() if b == [i,v]])
            break
    if m == v[0]:
        if d in v[1]:
            print(*[a for a,b in x.items() if b == [i,v]])
            break