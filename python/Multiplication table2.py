a = int(input())
b = int(input())
def jadvalzarb(a, b):
    for o in range(a, b):
        for i in range(a, b):

            print(i * o, '\t', end =' ')
        print( )  
jadvalzarb(a, b)