import math
# a*x^2 + b*x + c
def findX(a, b, c):
       x = (- b - (math.sqrt( (b * b) - 4 * a * c) ) / 2 * a)
       x2 = (- b + (math.sqrt( (b * b) - 4 * a * c) ) / 2 * a)
       return(x, x2)

martabe_a = int(input())
martabe_b = int(input())
sade = int(input())
natije = findX(martabe_a, martabe_b, sade)
print(natije)