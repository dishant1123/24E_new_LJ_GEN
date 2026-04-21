"""
simple  linear regression : use one independent variable (X) to predict one dependent variable (Y)

y= mx +c 
"""
# ex :1 

# import  numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# import  pandas as pd


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
# area , bedrooms 
"""
x = np.array([
    [1000,2],
    [1500,3],
    [2000,3], 
    [2500,4]
])
y= np.array([1500000,2000000,2600000,3200000])   # price =? 

model = LinearRegression()
model.fit(x,y)
print("predict price : \n",model.predict([[3000,4]]))  # 3775000  
"""
import  numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import  pandas as pd
import matplotlib.pyplot as plt

"""df = pd.read_csv("ML\housing.csv")

# convert  in to dataframe : 
# df = pd.DataFrame(data.data, columns=data.feature_names)
# df['price'] =data.target

# features  and target  : 

x= df.drop(['median_income'],axis=1)
y =df['median_income']

# spilt data  : 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# selection of  model  : 

model = LinearRegression()
model.fit(x_train, y_train)

print("predict price : \n",model.predict(x_test))
"""

# ex :4 

data =pd.read_csv("ML\Salary_Data.csv")
# print(data.head())

# print(data.isnull().sum())

# print(data.sample(5))

x=data[['YearsExperience']]
y=data['Salary']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

# predict : 
y_predict =model.predict(x_test)

compare = pd.DataFrame({
    "Years_Experience": x_test['YearsExperience'],
    "Actual_Salary": y_test,
    "Predicted_Salary": y_predict
}).reset_index(drop=True)
print(compare.head())


