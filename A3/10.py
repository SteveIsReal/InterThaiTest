
inputs = input().split()
count = 0
position = 0
while position != 0 and position != inputs[2]:
    if position + inputs[1] <= inputs[0]:
        position += inputs[1]
    else:
        position = (position + inputs[1]) - inputs[0]
    count += 1

print(count)
        
