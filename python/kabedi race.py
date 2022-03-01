a = [int(x) for x in input().split()]

userInput = [int(x) for x in input().split()]

count = 0
for i in userInput:
 if i <= 2 :
    count+=1

d = count//3
print(d)