from datetime import date
class Person():
    
    age = 60
    
    @classmethod
    def Age(cls):
        print('Age is : ', cls.age)

    


Person.Age()
