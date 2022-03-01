x = 0
x2 = 0
x3 = 0
while (x3 >= 0):
    x3 = int(input())
    if x3 < 0:
        break
    elif x3 > x2:
        x = x2
    elif x2 > x3:
        x3 = x2
        
    
print(x2, x)