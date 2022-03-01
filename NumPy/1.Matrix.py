import numpy as np

#araye do dar do matrix
a = np.array([[1, 2], [3, 4]])
print('a is:')
print(a)

#matrix do dar do
b = np.matrix([[1, 2], [3, 4]])
print('b is:')
print(b)

#zarb matrix dar khod
print(a@a)
print(np.dot(a, a))

#zarbb matrix dar khodash
print('multiply is: \n', np.multiply(a, a))

#variance
print('variance is: \n', np.var(a))

#paresh dar matrix
np.arange( 1, # -> az
10, # -> ta
3 # -> tedad martabe paresh
)
np.linspace(1, 10, 4)
