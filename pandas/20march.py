import pandas as pd
import numpy as np

df =pd.read_csv("pandas\mckinsey.csv")

print(df)
"""print(df.head())  #  1 st default  ==> 5 rows
print(df.tail())  # last  ==> 5 rows
"""
# new col  add : 

"""df["total_gdp"] =df['population']*df['gdp_cap']
print(df.head())
"""

# df= df.loc[df['year']==2002,['country',"life_exp"]]
# print(df)

# df=df.loc[df['life_exp']>28,['continent']]
# print(df)

# year ==2002 , country =='india' ,life_exp (sum):