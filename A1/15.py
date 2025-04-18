x,y,z = input(),input(),input()
if len(x) > 5 and len(y) > 5:
    print(x[:2]+y[len(y)-1]+z[len(z)-1])
else:
    print(x[0]+z+y[len(y)-1])