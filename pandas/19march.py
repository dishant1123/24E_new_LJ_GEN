import pandas as pd
import numpy as np

"""
task  :1 

1.create dataframe with id ,name,age,salary 
2.columns rename  col name  ==> name , first_name  
3.missing  np.nan  ==> drop 
4.missing  value  fill ==> age  int   ==> name ==> str 
5. con ==> salary  90000 and  id even   ==> name  

id   name  age     salary 
1    ram    23     90000
2    np.nan 45     23000
3    ramesh np.nan 98000
4    suresh 26     97000
5    riya   45     21000

"""
# sort_values  :

"""b=pd.DataFrame({
    "name":["raju","ramesh","ravan","riya","suresh"],
    "age":[12,13,14,15,10],
    "salary":[90000,10000,11000,12000,13000]
})
print(b)

# b.sort_values(by=['salary'],inplace=True)  # by default  ==> asc to desc 
# b.sort_values(by=['salary'],ascending=False,inplace=True)  # by default  ==> asc to desc 

# b.sort_values(by=['age','salary'],inplace=True)  # by default  ==> asc to desc 
# b.sort_values(by=['age','salary'],ascending=False,inplace=True)  # by default  ==> asc to desc
b.sort_values(by=['age','salary'],ascending=[True,False],inplace=True)  # by default  ==> asc to desc
print(b)
"""

# groupby  :

"""df =pd.DataFrame({
    "department" :["IT","HR","IT","HR","sales"], 
    "employees":["amit","raju","ramesh","ravan","riya"],
    "salary" :[10000,20000,30000,40000,50000]
})
print(df)
"""
# task  :1 
"""
sql : sum of salary for each department . 
sql : count of employees for each department .

sql : display department  wise salary  min salary , max salary  , sum salary , avg salary 

"""
# result = df.groupby("department")["salary"].sum()
# print(result)
# df.groupby("department")["employees"].count()

"""result = df.groupby("department")["salary"].agg(['sum','mean','min','max'])
print(result)

"""

"""df = pd.read_csv("pandas\mckinsey.csv")
print(df)
print(df.isnull().sum())
"""
