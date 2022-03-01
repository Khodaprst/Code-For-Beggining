class Karmand:
    
    raise_amnt = 1.05
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.gmail = first + '@gmail.com'
        Karmand.num_of_emp += 1
    
    def FullName(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)


class Developer(Karmand):
    raise_amnt = 1.06
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang
    def __repr__(self):
        return 'Developer ("{}, "{}", {})'.format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}, {}'.format(self.FullName(), self.gmail)
        
class Manager(Karmand):
    def __init__(self, first, last, pay, emps = None):
        super().__init__(first, last, pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps
    def ad(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)
    def rem(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)
    def prynt(self):
        for emp in self.emps:
            print('------>', emp.FullName())


dev1 = Developer('AmirHosein', 'Deist', 200, 'python')
emp1 = Karmand('Ali', 'moalemi', 200)
emp2 = Karmand('sara', 'sarae', 500)
mgr1 = Manager('mahdi', 'asghari', 600, [dev1])

print(repr(dev1)) #or # print(__repr__.dev1())
print(str(dev1)) #or # print(__str__.dev1())