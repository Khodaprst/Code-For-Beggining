answer = 0
tedad = 0
count = 0
for i in range (1, 11):
    number = int(input())
    for x in range(1, number +1):
        if number % x == 0:
            tedad += 1
        else:
            x = x +1
            
    if tedad > count:
        count = tedad
        answer = number

    elif tedad == count:
        if(number > answer):
            answer = number
            count = tedad
    tedad = 0
print(answer, count)