class Animal:
    def __init__(self):
        print('Animal class created!')

    def who(self):
        print('I am Animal')

    def Eat(self):
        print('I am eating')

class Dog(Animal):
    
    def __init__(self):
        super().__init__()
        print('class dog creatrd!')
    def who(self):
        print('I am Dog')
    def wagh():
        print('Wagh Wagh')

a = Dog()
a.who()