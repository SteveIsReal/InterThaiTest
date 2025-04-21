bubble = input().split()
tee = input().split()
tee_en = {'R':[12,18,25],
          'T':[15,20,30],
          'M':[10,15,20]
            }
bubble_en = {'H':5,'O':3,'J':2}
print(f'{(bubble_en[bubble[0]]*int(bubble[1])) + ((tee_en[tee[0]][int(tee[1])-1]) * int(tee[2]))}')
