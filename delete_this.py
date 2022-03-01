import random
import matplotlib.pyplot as plt

people = []
for i in range(0, 50):
    people.append(100)

for beshkan in range(0, 10000):
    for person1 in range(0, 50):

        person2 = random.randrange(0, 50)
        while people[person2] == 0:
            person2 = random.randrange(0, 50)
        
        if people[person1] != 0:
            people[person1] = people[person1] - 1
            people[person2] = people[person2] + 1

def rich_boy(a, b):
    a = b = int()
    return (a if a>b else b)

richest = max(people)
faqir = []
count = 0
cont = 0
for mardom in people:
    cont += 1
    if mardom == 0:
        count += 1
        faqir.append(cont)
#for faghir in faqir:
    #print('number', faghir, 'is out of game.')

fard = 0
for filtr in people:
    fard += 1
    if filtr == richest:
        break
print('people: \n', people)
print('this players has lost their money: \n', faqir)
print('at least,', count, 'people ended their money.')
print('the rich person is: \n number', fard, 'with', richest, 'dollars!')
tedad = people.count(richest)
if tedad == 1:
    print('and he is the richest. \ncongratulations!')
elif tedad >1:
    for filtr in people:
        while filtr <= fard:
            continue
        print(filtr)

