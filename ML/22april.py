# logistic regression : 
"""
categorial data  

ex : 
study_hrs    result 
2              0 
4              1
5              0
6              1
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
x= np.array([[1],[2],[3],[5],[6]])  # study  hrs 
y= np.array([0,0,0,1,1])   # result  pass or fail 

# model  : 
model = LogisticRegression()  # iteration = 900
model.fit(x,y)

# prediction  : 
print(model.predict([[4]]))  # 0 , 1 

# confusion  matrix :
"""                     predicted positive     predicted negative
actual positive           TP                     FN
actual negative           FP                     TN
"""
 
"""
1. precision :  TP  /  FP + TP     ==> 0.4 
     model  predict  pass value  : 3  
     actual pass value  : 2   
     precision  : 2/3  ===> 0.67 

| Student | Actual | Predicted |
| ------- | ------ | --------- |
| A       | Pass   | Pass      |
| B       | Fail   | Pass      |
| C       | Pass   | Pass      |
| D       | Fail   | Fail      |
| E       | Pass   | Fail      |

TP ==>pass  both   a and c 
FP ==> B
TN ==> D
FN ==> E 

2. recall (sensitivity)  : Tp/ tp +fn 
    out of all actual  positive , how many did model correctly find ? 

    actual  positive  : 3 
    model  predict  positive  : 2
    re call ==> 2/3 ==> 0.67
    
3. f1 score : 
        2 * (precision * recall) / (precision + recall)

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
