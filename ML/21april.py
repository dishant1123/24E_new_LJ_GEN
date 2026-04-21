"""
Polynomial Linear Regression : it is  extention of linear regression  where the relationship between input x and output y is non linear but still model use to linear equation in the terms of coefficients.

y = b0 + b1x + b2x^2 + b3x^3 + ....

use : 
1.data shown a curve pattern. 
2. linear regression give poor accruacy.

data set : 

x            y 
1            1
2            4 
3            9
4            16
5            25 

y = x^2 
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x =np.array([1,2,3,4,5]).reshape(-1,1)
y= np.array([1,4,9,16,25])

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

model = LinearRegression()
model.fit(x_poly,y)

y_pred = model.predict(x_poly)

plt.plot(x,y,label = "actual data")
# plt.scatter(x,y,label ="actual data")
plt.scatter(x,y_pred,label ="predicted data")
plt.legend()
plt.show()






