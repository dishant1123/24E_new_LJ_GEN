"""
# confusion  matrix :                     predicted positive     predicted negative
actual positive                             TP                     FN
actual negative                             FP                     TN

spam 
not spam 

Email     Actual    Predicted
1         spam      spam
2         notspam   spam 
3         spam      spam 
4         spam      notspam
5         not spam  not spam 
6         spam      spam 

2 find : Tp ,FP ,FN ,TN 

Tp   ==>(spam ==> spam) email 1 ,3, 6  ==> total  =3 
Fp   ==>(not spam ==> spam) email 2 
TN   ==>(not spam  ==> not spam) email 5 
FN   ==>(spam  ==> not spam) email 4 

precison  :  tp / (tp + fp)   ==> 3/4  ==>0.75 
recall :    tp / tp +fn       ==> 3 /4  ==> 0.75 
specificity : tn / tn + fp    ==> 1 /2  ==> 0.5
accuracy :   (tp + tn) / (tp + tn + fp + fn)  ==> 4/6 ==> 0.67

"""
"""
| Age | Income | Credit Score | Loan Approved |
| --- | ------ | ------------ | ------------- |
| 25  | 30000  | 600          | 0             |
| 40  | 60000  | 700          | 1             |
| 35  | 58000  | 650          | 1             |
| 28  | 32000  | 580          | 0             |
| 50  | 80000  | 720          | 1             |
| 23  | 25000  | 550          | 0             |

"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score
from sklearn.metrics import accuracy_score

# step :1 
"""data = {
    'Age': [25, 40, 35, 28, 50, 23],
    'Income': [30000, 60000, 58000, 32000, 80000, 25000],
    'Credit Score': [600, 700, 650, 580, 720, 550],
    'Loan Approved': [0, 1, 1, 0, 1, 0]
}
# step : 2 data  frame  ==> check  missing value 
df = pd.DataFrame(data)
print(df)

# stpe :3 target and features . 

x=df[['Income']]
y=df['Loan Approved']

# step :4 train test split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# step :5 model 
model = LogisticRegression()

# model fit : 
model.fit(x_train, y_train) 

# predict : 
y_pred = model.predict(x_test)

# accuracy :
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

"""

data  = pd.read_csv("train.csv")
# print(data.head())

# print(data.sample(10))

data = data[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare']]

data['Sex'] = data['Sex'].map({'male' :0,'female':1})

data['Age'].fillna(data['Age'].mean(),inplace=True)

# print(data.isnull().sum())

x = data.drop(['Survived'],axis=1)
y= data['Survived']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
# y_prob = model.predict_proba(x_test)

# print("y_pred :",y_pred)    
# print("y_prob :",y_prob)

print("accuracy :",accuracy_score(y_test,y_pred))

# confusion matrix : 

cm = confusion_matrix(y_test,y_pred)
print(cm)
"""
# confusion  matrix :                     predicted positive     predicted negative
actual positive                             TP                     FN
actual negative                             FP                     TN

"""
print("precision : ",precision_score(y_test,y_pred))
print("recall : ",recall_score(y_test,y_pred))
print("f1 score : ",f1_score(y_test,y_pred))
print("accuracy : ",accuracy_score(y_test,y_pred))
print("specificity : ",recall_score(y_test,y_pred,pos_label=0))

# knn , decison tree ,  random forest , SVM : 