# for & while har do iterate hastand va for az while estefade mikonad

lst = [1, 2, 3, 4]
my_iter = iter(lst)

# Amalkard marhale'E for
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())

#amalkard koli for:
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
