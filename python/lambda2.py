from re import X
from turtle import xcor


def multi(x):
    count = 1
    while x< 1000:
        x = x*2
        count += 1
        print(count, 'times repeated.\n', x)
        
x=1
while x<1000:    
    zarb = (lambda x: x*2) (x)
    x = zarb
    