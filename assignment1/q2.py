#a
import numpy as np
array = np.array([[1, -2, 3],[-4, 5, -6]])
abs_array = np.abs(array)
print(abs_array)

perc_25 = np.percentile(array, 25)
perc_50 = np.percentile(array, 50)
perc_75 = np.percentile(array, 75)
print(perc_25, perc_50, perc_75)

mean_val = np.mean(array)
median_val = np.median(array)
std_dev= np.std(array)
print(mean_val, median_val, std_dev)

#b
import numpy as np
a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])
floor_val= np.floor(a)
ceiling_val = np.ceil(a)
trunc_val = np.trunc(a)
round_val = np.round(a)

print(floor_val)
print(ceiling_val)
print(trunc_val)
print(round_val)

