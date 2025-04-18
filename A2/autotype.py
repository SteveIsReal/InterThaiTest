import time
x=[[0]]
b,v=0,0
while b < 10:
    while v < len(x):
        x.append([b])
        v += 1
    b += 1
    

# for i in range(10):
#     for j in range(len(x)):
#         x.append([i])

print(x)
print(time.process_time())