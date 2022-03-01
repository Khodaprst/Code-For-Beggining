class Karmand:
    
    raise_amnt = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.gmail = first + '@NABEGHEHA.COM'
        Karmand.num_of_emp += 1
    
    def FullName(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)


class Developer(Karmand):
    raise_amnt = 1.06
    def __init__(self, first, last, pay, lang):
        Karmand.__init__(self, first, last, pay)
        self.lang = lang


class Manager(Karmand):
    pass

dev1 = Developer('AmirHosein', 'Deist', 200, 'python')
dev2 = Karmand('Ali', 'moalemi', 200)

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)