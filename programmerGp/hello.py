class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        

h = Hello('AmirHosein')
print(h.a)
print(h._b)
