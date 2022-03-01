class A:
    def __init__(self,):
        print('class first')


class B:
    def __init__(self, noob, game):
        self.noob = noob
        self.game = game
        print('class second')


class C(A, B):
    def __init__(self):
        print('class Third')
        B.__init__(self, 'fifa', 'Gow')
        A.__init__(self)
#dastoor super() hamishe avaling onsor ra mikhanad
n = C()