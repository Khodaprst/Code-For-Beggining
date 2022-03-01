#tuple to list
names = ('Amir', 'Ali', 'Mmd')
names = list(names)
print(names, type(names))

#tuple to string
names = ('Amir', 'Ali', 'Mmd')
names = ' '.join(names)
print(names, type(names))

#string to list
name = 'Amir'
name = name.split()
print(name, type(name))

#string to tuple
#1
name = 'Amir'
name = tuple(name)
print(name, type(name))
#2
str = "Amir, Ali, Mmd"
str = eval(str)
print(type(str))

#list to string
names = ['Amir', 'Ali', 'Mmd']
names = ' '.join(names)
print(names, type(names))

#list to tuple
names = ['Amir', 'Ali', 'Mmd']
names = tuple(names)
print(type(names))