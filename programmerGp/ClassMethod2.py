from datetime import date
class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def Year(cls, name, Year):
        return cls(name, (date.today().year - Year))        

    
    def display(self):
        print(f'Hello, I am {self.name}, and I am {self.age} years old.')
    
    
p = Person('Amir', 21)
q = Person.Year('Amir', 2000)
q.display() 