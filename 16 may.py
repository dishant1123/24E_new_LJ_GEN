#guess the number  : 

"""
computer   num: 1, 20 ==>  6  

5 attempt : 4 low   16 high   7 low   19 high  6 congrats 

"""
import random as r 

max_attempt = 5 
com_guess = r.randint(10,20)   # 15 
flag = 0
while  max_attempt >0 :
    user_num = int(input("enter the num  :  "))
    if user_num ==com_guess:
        print("congrats .....u win .")
        flag=1
        break
    elif user_num > com_guess :  # 12  > 15 
        print("too high")
    elif user_num < com_guess :
        print("too low")
    
    max_attempt-=1 
if flag==0:
    print("guess num is  : ",com_guess)