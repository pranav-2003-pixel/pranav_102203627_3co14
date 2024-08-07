#q1 a
import numpy as np
arr = np.array([1,2,3,6,4,5])
print(np.flip(arr))

#b
import numpy as np
array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
print(np.ravel(array1))
print(np.ndarray.flatten(array1))

#c
import numpy as np
arr1 = np.array([[1, 2], [3, 4]]) 
arr2 = np.array([[1, 2], [3, 4]])
print(np.array_equal(arr1,arr2))

#d
import numpy as np
x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
a = np.bincount(x).argmax()
b = np.bincount(x).argmax()
c = np.where(x==a)
d = np.where(y==b)
print(a,c)
print(b,d)

#e
import numpy as np
gfg = np.matrix('[4,1,9;12,3,1;4,5,6]')
total_sum = np.sum(gfg)
print(total_sum)
row_sum = np.sum(gfg,axis=1)
print(row_sum)
col_sum = np.sum(gfg, axis = 0)
print(col_sum)

#f
import numpy as np
n_array = np.array([[55, 25, 15],[30, 44, 2],[11, 45, 77]])
diag_sum = np.trace(n_array)
print(diag_sum)
eigenvalues, eigenvectors = np.linalg.eig(n_array)
print(eigenvalues,eigenvectors)
inverse_matrix = np.linalg.inv(n_array)
print(inverse_matrix)
det_matrix = np.linalg.det(n_array)
print(det_matrix)

#g
import numpy as np
p1 = np.array([[1, 2], [2, 3]])
q1 = np.array([[4, 5], [6, 7]])
product_1 = np.dot(p1, q1)
covariance_1 = np.cov(p1, q1)
print(product_1,covariance_1)

p2 = np.array([[1, 2], [2, 3], [4, 5]])
q2 = np.array([[4, 5, 1], [6, 7, 2]])
product_2 = np.dot(p2, q2)
p2_flat = np.ndarray.flatten(p2)
q2_flat = np.ndarray.flatten(q2)
covariance_2 = np.cov(p2_flat,q2_flat)

#h
import numpy as np
x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])
inner_product = np.inner(x, y)
print(inner_product)
outer_product = np.outer(x, y)
print(outer_product)
cartesian_product = np.cross(x, y)
print(cartesian_product)




