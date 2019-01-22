import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
print(x[1])
y = np.array([2.0,4.0,6.0])
print(x+y)
print(x-y)
print(x*y)
z = np.array([[[1.0,2.0],[1.0,3.0]],[[2.3,3.0],[4.0,9.0]]])
print(z)
a = np.array([1,2])
print(z*a)
b = np.array(list([1,"abc",0.1]))
print(b)
print(type(b[0]))
b[0]=10000
print(b)
print(type(b[0]))
print(b.shape)
print(z[0])
a = np.empty([2,3])
print(a)
a = np.arange(0, 30, 2)
print(a)
a.resize(8,3)
print(a)
a = np.arange(0,10,2)
b = a
print(a)
c = a[0:2]
c =[100,100]
print(a)
print(b)
a[0:2]=[100,100]
print(a)
print(b)