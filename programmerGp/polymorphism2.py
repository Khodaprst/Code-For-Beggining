class Dog:
    def Sound(self):
        print('Wagh Wagh')

class Cat:
    def Sound(self):
        print('Meow Meow')

def SoundMaker(Animal):
    Animal.Sound()

Rexi = Dog()
Heli = Cat()

SoundMaker(Heli)

#هر تابعی () دارد که باید متغیر هایی داخلش تعریف شود.
#تابع آخری که نوشته شد به دو ابع فوق خود رابط شد بطوری که 
#Animal.Sound
#در تابع هایی صدق میکرد که از تابع 
#Sound
#در آنها تعریف شده باشد، بنابراین در توابع که این دستور تعریف شده میتوان شناسه هایی مشخص کرد
#و با آن شناسه ها از تابع خود استفاده کرد


