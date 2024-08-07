#a
import numpy as np
array = np.array([10, 52, 62, 16, 16, 54, 453])
sorted_array = np.sort(array)
print(sorted_array)
ind_sorted_array = np.argsort(array)
print(ind_sorted_array)
sm_4 = np.sort(array)[:4]
print(sm_4)
lar_5 = np.sort(array)[-5:]
print(lar_5)

#b
import numpy as np
array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
int_elmt = array[array == array.astype(int)]
print(int_elmt)
flt_elmt = array[array != array.astype(int)]
print(flt_elmt)

