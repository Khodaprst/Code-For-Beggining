import random
hads = random.randint(1, 99)
print(hads)
list = ['k', 'b', 'd']
javab = input()
while javab !='d':
    if javab == 'b':
        adadeA = hads
        hads = random.randint(adadeA, 99)
        print(hads)
        javab = input()
    elif javab == 'k':
        adadeB = hads
        hads = random.randint(1, adadeB)
        print(hads)
        javab = input()
    else:
        break