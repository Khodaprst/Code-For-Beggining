import numpy as np

# np.array([zarib aval, zarib dovom, haman adad sabet])
#           x^2       + 2x         + 2
# x^2 + 2x + 2

moadele = np.array([1, 2, 2])

# np.polyval(moadele, adad jaygozin x)
np.polyval(moadele, 1)

#moshtaq
np.polyder(moadele) # -> [2, 2] -> 2x + 2

#integral
print(np.polyint(moadele)) # -> [0.33333333, 1,  2,  0] -> x^3/3 + x^2 + 2x + 0