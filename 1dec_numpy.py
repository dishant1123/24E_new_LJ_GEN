# numpy : 
"""
1. python library
use : 
1. array manupulation  , sort  update remove 
2. matrix multiplication, manupulation
3. linear algebra
"""

#pip install numpy 

import numpy as np 

"""a=np.array([1,2,3,4,5])
print(a)
print(type(a))
print(a.ndim)  # number of dimension
"""

# b=np.array([1,2,3,4,5,"saloni"])
# print(b)

# c=np.array(['1','2','3','4','5','78.90'],dtype=str)
# print(c)

# d=np.array([1,2,3,4,5,78.90,True],dtype=float)
# print(d)

"""b=np.array([[1,2],[4,5],[7,8]])
print(b)
print(b.ndim)
print(b.shape)
"""

# c=np.arange(10)
# c=np.arange(0,10,2)
# print(c)

"""d=np.arange(1,21).reshape(5,4)
print(d)
"""

a=np.array([
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [15,16,17,18,19,20,21],
    [22,23,24,25,26,27,28]
])

# print(a)
# print(a[0])
# print(a[1:3])
# print(a[1:3,2:4])
# print(a[1, : : 2])
# print(a[2:4, : :-1 ])

# array manipulation: 
# a[2 :7] =900
# a[1:3,2:5]=100
# print(a)
"""
task  :1 

[[8,9],
[15,16]] 

task :2 

[[6,7],
[20,21],
[27,28]]

"""
"""
a=np.array([
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [15,16,17,18,19,20,21],
    [22,23,24,25,26,27,28]
])"""
# print(a[[0,2,3],5:7])

# array([2,10,18,26])
# print(a[[0,1,2,3],[1,2,3,4]])

# random  array  :
import random as r 

# a= np.random.randint(low=-10, high=10,size=12).reshape(3,4)
# a= np.random.randint(low=-10, high=10,size=(3,4))
# a= np.random.random(size=(3,4))
# print(a)

a=np.array([
    [11,2,3,4],
    [80,9,10,11],
    [15,164,17,18]
])

# print(a.sum())  # sum of all elements
# print(a.sum(axis=0))  # col wise sum 
# print(a.sum(axis=1))  # row wise sum 

# print(np.sort(a))
# print(np.sort(a,axis=0))
# print(np.sort(a,axis=1))

