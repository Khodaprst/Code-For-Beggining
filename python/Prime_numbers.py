a =[]
c = 0
x = int(input())
while x != 0:
    for i in range(1, x):
        if (x % i == 0):
            c+=1
    if (c == 1):
        print('prime')
        a.append(x)
    else:
        print('not prime')
    x = int(input())
    c = 0
print(a)