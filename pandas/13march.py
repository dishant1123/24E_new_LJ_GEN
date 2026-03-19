import pandas as pd

"""b=pd.DataFrame({
    "name":["raju","ramesh","ravan","riya","suresh"],
    "age":[12,13,14,15,16],
    "salary":[90000,10000,11000,12000,13000]
})
"""
"""
task :1
     name    age salary  
0     raju    12  90000
1    ramesh    13  10000
2    ravan     14  11000
3     riya     15  12000
4   suresh     16  13000

task :2  name  salary  

"""

# loc  : 
# iloc : 

b=pd.DataFrame({
    "name":["raju","ramesh","ravan","riya","suresh"],
    "age":[12,13,14,15,16],
    "salary":[90000,10000,11000,12000,13000]
})
print(b)
# print(b.loc[0])
# print(b.iloc[0])

# print(b.loc[1 :4])  # last included 
# print(b.iloc[1 :4])  # last excluded 
# print(b.iloc[1:4,1:3])
# print(b.loc[1:4,"name":"salary"])

# print(b.iloc[[0,2,3],[1,2]])

"""
task :3 display age > 14  name salary print 
task  :4 display  person   who's name  startwith  'r' 
"""

b =b.loc[b['age']>14],['name','salary']
print(b)

# b=b.iloc[(b['age'] >14).values,[0,2]]
# print(b)



