import numpy as np
x = np.array([[2,1],[1,2]])
print(x)

xt = x.transpose()
print(xt)
print('=============================')
x2 = xt.dot(x)
print(x2)
print('==============================')
import numpy.linalg as lg

s = lg.inv(x2)
print(s)
print('=================================')


