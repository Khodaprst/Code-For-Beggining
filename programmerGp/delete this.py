class ProgrammerGp():
    def __init__(self, name, fan, major, programming, job):
        self.name = name
        self.fan = fan
        self.major = major
        self.Program_path = programming
        self.Job = job

    def sentence(self):
        print(f'your name is {self.name} and you are programming {self.Program_path}.')

    def fohsh(self):
        return f'Kose Amat! {self.name}'

Amir = ProgrammerGp('AmirHosein', 'BreakingBenjamin', 'Engineering', 'Python', 'Biomedical Engineer')
Mhmd = ProgrammerGp('Mohamad Amin', 'Skillet', 'Chemical', 'Python', 'Programming')
Hosein = ProgrammerGp('Hosein', 'five Finger Death Punch', 'Physic', 'C ', 'Astronaut')

print(Hosein.Program_path)
print('snoop dog!')
ProgrammerGp.sentence(Amir)
print(ProgrammerGp.fohsh(Mhmd))