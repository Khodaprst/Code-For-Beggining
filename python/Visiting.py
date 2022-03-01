y = []
x = input()
x = x.split()

for i in range(0, len(x)):
    x[i] = float(x[i])
x.sort()

y.append(x[2]-x[1])
y.append(x[2]-x[0])
y.append(x[1]-x[0])
y.sort()

if ((y[0]+y[1]).is_integer() == True):
    print(int(y[0]+y[1]))
else:
    print (y[0]+y[1])