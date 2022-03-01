import numpy as np

# Define a matrix A
A = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype=float)
b = np.array([1,2,3], dtype=float)
print('matrix A: \n', A, 'vector b: \n', b)

from scipy import linalg
x = linalg.solve(A, b)
print('answer is: ', x)
print('Check values, np.dot(A, x) = ', np.dot(A, x))
print('Check values, b = ', b)
print('Check values, ', np.allclose(np.dot(A, x), b))

print('------------------------------------------------------------------------------')
B = np.random.random((3,3)) * 10
x = linalg.solve(A, B)
x_np = np.linalg.solve(A, B)
print('answer is: ', x)
print('answer from Numpy is: ', x_np)
print('Check values, np.dot(A, x) = ', np.dot(A, x))
print('Check values, B = ', B)
print('Check values, ', np.allclose(np.dot(A, x), B))

print('------------------------------------------------------------------------------')
from scipy.linalg import eigh
w, v = eigh(A, subset_by_index=([1,1]))
print('eigenvalue: ', w, '\n eigenvector: ', v)
# inverse, determinant of A
A_inv = linalg.inv(A)
A_det = linalg.det(A)
print('A_inv: ', A_inv, '\n A_det: ', A_det)
#-- the norm 
from scipy.linalg import norm
A_fro = norm(A, 'fro')
# 2-norm
A_2_norm = norm(A, 2)
print('A_fro: ', A_fro, '\n A_2_norm: ', A_2_norm)

print('------------------------------------------------------------------------------')
from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,3)
# generate random numbers from poissonian
mu = 4
x = poisson.rvs(mu, size=1000)
ax[0][0].plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax[0][1].plot(x, poisson.cdf(x, mu), 'bo', label='poisson cdf')
ax[0][2].hist(x, density=True, histtype='stepfilled', alpha=0.2, label='poisson hist')

x_norm = norm.rvs(mu, size=1000)
ax[1][0].plot(x_norm, norm.cdf(x_norm, mu), 'bo', label='norm cdf')
ax[1][1].plot(x_norm, norm.cdf(x_norm, mu), 'bo', label='norm cdf')
ax[1][2].hist(x_norm, density=True, histtype='stepfilled', alpha=0.2, label='poisson hist')

plt.show()

print('Test if two sets of (independent) random data comes from the same distribution, ', ttest_ind(x, x_norm))
