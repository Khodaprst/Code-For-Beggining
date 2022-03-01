class Shark:
    def Swim(self):
        print('Shark is swimming')
    def SmwimBack(self):
        print('Shark cannot swim backward')
    def Skeleton(self):
        print('Shark has big Skeleton')

class ClownFish:
    def Swim(self):
        print('ClownFish is swimming')
    def SmwimBack(self):
        print('ClownFish cannot swim backward')
    def Skeleton(self):
        print('ClownFish has small Skeleton')
    
def ocean(fish):
    fish.Swim()
    
tommy = Shark()
jimmy = ClownFish()

ocean(tommy)
