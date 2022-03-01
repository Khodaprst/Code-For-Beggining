import random
class Payment:
    takhfif = random.randint(10, 100)
    def __init__(self, money):
        self.__money = money

    def __discounter(self):
        print(f'congratulation! you have {Payment.takhfif}% discounter')

    def setter(self, discount):
        if (discount == 'ghorban 99'):
            self.__money = self.__money - (self.__money * (Payment.takhfif/100))
            self.__discounter()
        else:
            print("sorry, you don't have any discounter")
    def getter(self):
        #getter = final price
        return self.__money

dvd = Payment(30)
dvd.setter('ghorban 99')

print(dvd.getter())
