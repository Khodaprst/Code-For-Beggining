class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('this is getter')
        return self.__name

    @name.setter
    def name(self, name):
        print('this is setter')
        print(f'setting name to {name}')
        self.__name = name

    @name.deleter
    def name(self):
        print(f'this is deleter and {p.name} has deleted')
        del self.__name

p = Person('AmirHosein')
print(f'the name is {p.name}')
p.name = 'Mhmd'
print(f'the name is {p.name}')
del p.name
