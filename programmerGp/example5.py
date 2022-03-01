class Circle:
    def __init__(self, r):
        self.radius = r

    def Masahat(self):
        return self.radius ** 2 * 3.14
 
    def mohit(self):
        return 2*self.radius

NewCircle = Circle(8)

print(NewCircle.Masahat())
print(NewCircle.mohit())