import pandas as pd
import numpy as np
# join  : 

"""
1. inner ==> 2 table 1 col common 
2. outer  ==> 
3. left ==> left side only   
4. right ==> right side only 
5. cross ==> all table  merger ==> not mendatory for common col
"""

users =pd.DataFrame({
    "USER_ID" :[ 1,2,3], 
    'NAME':["John","Mary","Tom"],
    
})
# print(users)

msgs= pd.DataFrame({
    "USER_ID" :[ 1,1,2,4],
    "MSG":['hello','hi','how are you','bye']
})
# print(msgs)  # user_id

# concat  : 
"""result = pd.concat([users,msgs])
result = pd.concat([users,msgs],axis =0)
result = pd.concat([users,msgs],axis =1)

print(result)
"""
# merge :   inner join  

# result =users.merge(msgs)
# print(result)

# users.rename(columns={'USER_ID':'id'},inplace=True)
# print(users)  # id 
# result =users.merge(msgs)  # it give  error  bcz  not match col name . 

# result = users.merge(msgs,left_on='id',right_on='USER_ID')
# print(result)


# how  = inner , left ,right  : 

# result = users.merge(msgs,left_on='id',right_on='USER_ID',how="left")
"""
 id  NAME  USER_ID          MSG
0   1  John      1.0        hello
1   1  John      1.0           hi
2   2  Mary      2.0  how are you
3   3   Tom      NaN          NaN
"""
# result = users.merge(msgs,left_on='id',right_on='USER_ID',how="right")
"""
    id  NAME  USER_ID          MSG
0  1.0  John        1        hello
1  1.0  John        1           hi
2  2.0  Mary        2  how are you
3  NaN   NaN        4          bye
"""
# result = users.merge(msgs,left_on='id',right_on='USER_ID',how="outer")
"""
   id  NAME  USER_ID          MSG
0  1.0  John      1.0        hello
1  1.0  John      1.0           hi
2  2.0  Mary      2.0  how are you
3  3.0   Tom      NaN          NaN
4  NaN   NaN      4.0          bye
"""
# print(result)

movies = pd.read_csv("pandas\movies.csv")
print(movies)