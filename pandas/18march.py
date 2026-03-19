import pandas as pd
import numpy as np

"""
axis =1  ==> col 
axis =0  ==> row 
"""

# df =pd.DataFrame([[0,1,2,np.nan,5],[2,0,1,5,np.nan],[5,0,1,np.nan,5],[2,0,1,np.nan,np.nan]])

# df=df.drop_duplicates(subset=[0])
# df=df.drop_duplicates(subset=[1,2])
# df=df.drop_duplicates(subset=[3,4])
# df=df.drop_duplicates(subset=[0,1])

# df =df.dropna(thresh=2,axis=1)
# df =df.dropna(thresh=4,axis=0)

# df =df.dropna(axis=1)
# print(df)
"""
   0  1  2    3    4
0  0  1  2  NaN  5.0
1  2  0  1  5.0  NaN
2  5  0  1  NaN  5.0
3  2  0  1  NaN  NaN
"""
# u all   s 01,   j 0,1    h d  0 1 3  


# df=pd.DataFrame({"a":[1,2,np.nan,3,4],"b":[1,5,np.nan,2,1]})
# df = df.drop_duplicates(subset="b")
# df.dropna()
# df.fillna(20,inplace=True)
# print(df.shape[1])
# print(df)

# 2 : csv read ,sort_values , filter ==> lambda ,

