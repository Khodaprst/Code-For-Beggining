class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.color = color

    def setter(self, value):
        self.__speed = value
        

    def getter(self):
        return self.__speed

peykan = Car(100, 'red')
peykan.setter(150)

print(peykan.getter())

