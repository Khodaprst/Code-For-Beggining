dama_ha = [2, 5, 8, 13, 15, 19]

celsius_to_fahrenheit = map(lambda x: (x*9/5) + 32, dama_ha)
print(list(celsius_to_fahrenheit))

#----------------------------------------------

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
jam = map(lambda x,y,z: x+y+z, lst1,lst2,lst3)
print(list(jam))