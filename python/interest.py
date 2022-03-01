x = input ('number: ')
x = int(x)
c = 0
for i in range(1, x):
    if (x % i == 0):
        c+=1
print(c)
javab = input('you want to try again? ')
while javab == ('yes'):
    x = input ('number: ')
    x = int(x)
    c = 0
    for i in range(1, x):
        if (x % 1 == 0):
            c+=2
    print(c)

else:
    print('the end')
