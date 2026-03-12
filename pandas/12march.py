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
"""e=pd.Series([12,45,99,67,89,90,56,89,133],index=['a','b','c','d','e','f','g','h','i'])

print(e)
print(e.head(2))  # by default  5 rows 
print(e.tail(2))  # by default  5 rows  last 
print(e.head(-1))
print(e.tail(-1))
print(e.tail(-11))
print(e.tail(-8))
print(e.head(-8))

"""
"""
f=pd.Series([21,22,23,24,25],index=['ram','raju','ramesh','ravan','riya'])
print(f)
print(f.sample(3))
print(f+1)
print(f-1)
print(f*2)
print(f/2)
"""

"""g=pd.Series([10,20,30,0,None,40,None,50])

print(g)
# print(g.isnull())
# print(g.isnull().sum())
print(g.notnull())
print(g.notnull().sum())

g=g.fillna(0)
print(g)
"""

"""f=pd.Series([234,22,23,24,0.9],index=['ram','maju','mamesh','avan','iya'])

print(f)
# print(f.sort_values())  # asc to desc 
# print(f.sort_values(ascending=False))  # desc to asc

print(f.sort_index())
print(f.sort_index(ascending=False))
"""

# dataframe : 

"""a=pd.DataFrame([
    [1,"raju",12,90000],
    [2,"ramesh",13,10000],
    [3,"ravan",14,11000],
    [4,"riya",15,12000],
    [5,"suresh",16,13000]],
columns=['id','name','age','salary'])
print(a)
"""
b=pd.DataFrame({
    "name":["raju","ramesh","ravan","riya","suresh"],
    "age":[12,13,14,15,16],
    "salary":[90000,10000,11000,12000,13000]
})
# print(b)
# print(b.rename(columns={"name" :"first_name"}))
b['id'] = range(1,6)
b['salary'][0] =50000
b.drop(columns=['salary'],inplace=True)
print(b)
