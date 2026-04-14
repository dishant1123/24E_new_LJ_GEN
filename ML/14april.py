"""
simple  linear regression : use one independent variable (X) to predict one dependent variable (Y)

y= mx +c 
"""
# ex :1 

import  numpy as np
from sklearn.linear_model import LinearRegression
"""
# one feature area : 

x = np.array([[1000],[1500],[2000],[2500]])  # 3000 
y= np.array([1500000,2000000,2500000,3000000])   # price =? 

# model  : 
model = LinearRegression() 
model.fit(x,y)

# predict : 
print("predict price : \n",model.predict([[3000]]))

"""

# ex :2 multiple linear regression : use  more than one  independent variable . 

x = np.array([
    [1000,2],
    [1500,3],
    [2000,3], 
    [2500,4]
])

# 3000 
y= np.array([1500000,2000000,2500000,3000000])   # price =? 
