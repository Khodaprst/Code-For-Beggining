#lambda
MyFunc = lambda x : x*2
print(MyFunc(4))

#---------------------------

#map
lest = [2, 4, 5, 9]
print(list(map(MyFunc, lest)))

#or

print(list(map(lambda x: x/2 , lest)))

#----------------------------

#filter

print(list(filter(lambda x: x%2 == 0, lest)))