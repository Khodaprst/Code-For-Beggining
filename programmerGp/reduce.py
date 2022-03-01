from functools import reduce

lst = [1, 5, 6]
maks = lambda x,y: x if (x>y) else y

print(reduce(maks, lst))