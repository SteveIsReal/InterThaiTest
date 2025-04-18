v = 0
while (x:=int(input())) != 5:
    v += 100 if x == 1 else 120 if x == 2 else 200 if x == 3 else 60 if x == 4 else 0
print(f'Bye Bye\nTotal Calories: {v}')