class Man:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def sleep(self):
        slip = (self.first_name, 'wanna sleep')
        return (' '.join(slip))

    def run(self):
        ron = (self.first_name, 'is running')
        return (' '.join(ron))

class Teacher(Man):
    def __init__(self, first_name, last_name, evidence, university):
        self.first_name = first_name
        self.last_name = last_name
        self.evidence = evidence
        self.university = university

Me = Teacher('Amir', 'Khodaprst', 'Biomedical Engineer', 'Imam Reza')
print(Me.sleep())
print(Me.run())