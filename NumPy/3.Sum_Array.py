import numpy as np


array_2D = np.array([[1, 2], [3, 4]])
print(array_2D, '\n'*2)
#jam kole maghadire matrix
np.sum(array_2D)

#jam'e mesle fibonachi dar matrix
np.cumsum(array_2D)

#jam'e sotun ha va namayesh an dar satr akhar
np.cumsum(array_2D, axis=0)

#jam'e satr ha va namayesh an dar sotun akhar
np.cumsum(array_2D, axis=1)

#tafrigh 2 array
np.subtract(array_2D, array_2D)

#taghsime 2 array
np.divide([5, 6, 7], 3)
#gerd kardan adad ashar
np.floor_divide([5, 6, 7], 3)

#jazr
np.math.sqrt(5)

#tolid adad random ((beyn)  adad,(ta) akhar, (tedad satr, tedad sotun))
np.random.uniform(1, 5, (2, 3))
print(np.random.standard_normal((2,         #satr
 1)))          #sotun       