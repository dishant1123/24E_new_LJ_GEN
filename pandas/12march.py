"""
pandas :pip install  pandas  

1. data cleaning  : 
2. data analysis  :

==> join , group by , sort , where
"""

import pandas as pd

"""a= pd.Series([12,13,14,15,17,189])
print(a)

b= pd.Series([12.56,12.89 ,67.90])
print(b)

c=pd.Series(['a','b','c','d','e','f'])
print(c)

d=pd.Series([12,34.67,"yash"])
print(d)
"""

"""e=pd.Series([12,45,67,89,90],index=['a','b','c','d','e'])
print(e)
print(e.shape)
print(e.dtype)
print(e.values)
print(e.index)
print(e.keys())
print(e.info())
print(e.describe())
"""
# drop : 
"""
e=pd.Series([12,45,None,67,89,90],index=['a','b','c','d','e','f'])
print(e)
print(e.isnull().sum())
# print(e.dropna())  # remove  missing value
print(e.fillna("90"))
"""

# head,  tail  : 
e=pd.Series([12,45,99,67,89,90,56,89,133],index=['a','b','c','d','e','f','g','h','i'])

# print(e)
# print(e.head(2))  # by default  5 rows 
# print(e.tail(2))  # by default  5 rows  last 
# print(e.head(-1))
# print(e.tail(-1))
# print(e.tail(-11))
# print(e.tail(-8))
print(e.head(-8))

