
"""
You've been given a dataset with apartment area and price information. There's a noticeable non-linear relationship between 
area and price. To address this you intend to categorize them into 'High', 'Medium', and 'Low' groups. Prices above $3,000,000 
are 'High', below $2,000,000 are 'Low', and between $2,000,000 and $3,000,000 are 'Medium'. Write a code to achieve this 
assuming that dataset has two columns named area and price.


"""
import  pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'area' :[1000,1500,2000,2500,3000,3500],
    'price':[1500000,2200000,2700000,3200000,3400000,3800000]
    
})

# feature  and target : 
x = data[['area']]
y= data['price']

# train_test_split :

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=42)

# model  fit 
model = LinearRegression()
model.fit(x_train, y_train)

# prediction  : 

y_pred = model.predict(x_test)

print("x_test :\n",x_test)
print("actual  price : \n",y_test)
print("predicted price : \n",y_pred)



"""
id    movie           rating    budget 
1      KGF             8         high
2      PK              7         medium
3      RRR             8.5       high
4      Dhurandhar      6         avg       

babie 7.5  ==> 
"""
