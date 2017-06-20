from numpy import *
ar1 = ones((5, 4))
print(ar1)
ar2 = zeros((5,1))
ar2[0] = 1
print(ar2)
print(str(ar1 * ar2))
ar1[1, 2] = 10
ar1 *= 2
print(ar1)
print(ar1.sum())
print(ar1.sum(axis=1))
print(ar1.sum(axis=0))
