import random
random.seed()


people = []
for i in range(0, 50):
    people.append(100)
    
for beshkan in range(0, 100000):
    for person1 in range(0, 50):
        person2 = random.randrange(0, 50)
        while people[person2] == 0:
            person2 = random.randrange(0, 50)
        if people[person1] != 0:
            people[person1] = people[person1] - 1
            people[person1] = people[person1] + 1

print(people)