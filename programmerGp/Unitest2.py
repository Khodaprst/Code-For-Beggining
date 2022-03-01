class Karmand:
    ''' A sample Class'''

    raise_amnt = 1.05
    

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def FullName(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)


