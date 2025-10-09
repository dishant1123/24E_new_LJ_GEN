# power  : 

# print(type(2.5**4))

"""
l1 =90 
print(type(l1))
"""

"""s1="sdd"
print(type(s1))
"""
# s2 =input("enter the string  : ")
# ord : ===> converts the characters of a string to their ASCII values 
# print(ord(s2))

"""if s2 >='A' and s2 <='Z' :
    s2 =ord(s2) +32 
    print(chr(s2))
else: 
    s2= ord(s2) -32 
    print(type(chr(s2)))
    # print(type(s2))
"""
"""s3='a'
print(type(s3))"""

"""print(10/3)
print(10//3)
"""
# print(3*5/5)

"""
a_b_c =10000 ,20000, 30000
print(a)
print(b)
print(c)
"""

"""class a : 
    name  ="saloni" 
    __age =90

b=a() 
print(b.name)  
print(b.__age)
"""
# print(2 ==2.0) 

"""a=float(input("enter the number  : "))
print(a)
"""

"""_ = '1 2 3 4 5 6'  
print(_)
"""

# print(print(print("python")))
"""a=0
b=6
x=(a or b) or  ((a and a) or (a and b))
print(x)
"""

"""a=14
b=14
x=(a or b) or ((a and a) or (a and b))
y=not(0)
print(y)
"""

#  What will be the output of this program?
# print(True ** False / True) 

# a=True 
# print(type(a))

"apple"=="mango"  
"""
a. name error 
b. type  error 
c. syntax error 
d. value error
"""

# print("apple"="ma/ngo")

# print(3 *3 **3 )
# print("hello" + "-" + "how" + "-" + "are" + "you")

# print((7*5**2)/True*False)

# print(int(6 == 6.0) * 3 + 4 % 5)
# of this program?
# print(6 + 5 - 4 * 3 / 2 % 1) 

"""
Write a Python program to find an integer exponent x such that a^x = n.
 Input:
 a =  2 : n =  1024
 Output:
 10
 Input:
 a =  3 : n =  81
 Output:
 4
"""
import  math as m  

# n=int(input("enter the number  : "))  # 1024  
# a=int(input("enter the base  : "))  # 2 

# count =0 

# while n!=0 :   # 1024 ! =0 
#     result = n //a   # result = 1024 /2 =512 
#     count+=1   # count =1 
#     n = result   # n =512 

# print("count  :",count)

"""n = int(input("Enter the number  : "))   # Example: 1024
a = int(input("Enter the base  : "))     # Example: 2

count = -1

while n > 0:  
    result = n // a       # use integer division
    count += 1
    n = result

print("Count :", count)
"""

"""if 4 + 5 == 10:
    print("TRUE")
else:
    print("FALSE")
print("TRUE")
"""
# het    harshil   devam 

"""x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")

"""
"""x = 3
if (x > 2):
    x = x * 2  # x =6 
if (x > 4):# 6 > 4 
    x = 0   # x =0 
print(x)
"""

"""a = 3
b = (a != 3)
print(b)
"""
# het  false devam false   

"""x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 4
print(x)
"""
# het   devam   har  
"""x = 2
a = 5
b = 5
if a > 0:  # 5 > 0 
    if b < 0:   # 5 < 0 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
"""
# harshil : 5  het:5   devam : 5 
"""
n=7
c=0
while(n):    
    if(n>5):   
        c=c+n-1    
        n=n-1      
    else:
        break
print(n)
print(c) """

# ans : het : 11 ,5   devam 0 , 28  harshil  :  42 ,+42 
# saloni  5 11     jaival   rishi     utsav 

"""var = 10
for i in range(10):  # 2 , 9 
    for j in range(2, 10, 1):  # 9,10   # 2 -9  
        if var % 2 == 0:    # 10 % 2==0 
            continue      
            var += 1
    var+=1  # var =13 
else:
    var+=1
print(var)
"""
# rishi :10   utsav : 21  jaival :   het: 31  devam : 21 saloni : 

"""for i in range(0,2,1):
    print("heelooo")

for x  in range(100,0,-1):
    print(x,end=" " )
"""
"""for i in range (5, 0, -2):
    print(i)

print(range(5, 0, -2))

print(range(5, 0, -2))"""

"""for i in range(-2, -5,-1):
    print(i)
"""

"""x = 12
for i in x:
    print(i)
"""
"""x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x) # 1- 90 
print(x) # 90 
"""

"""for num in range(2,-5,-1):
    print(num, end=", ")
"""
"""x = 0   # 0 
while (x < 100):  # 100  < 100 
  x+=2    # x =x +2 x =2 4  .. 98  100  
print(x)
"""
"""for num in range(10, 14):
   for i in range(2, num):
       if num % i == 1:
          print(num)
          break
"""
# 10 11 12 13 
"""x = 2
for i in range(x):  # 1 ,2 
    i-= 2       # x = 0-2 =2  
print (i)   # 0 ,-2 
"""
# 
    
"""a = 53
b = 5.0
print('yes') if (a == b) else print('no')
"""
# a=b=0
"""a,b =0
print(a,b)
"""
a =123 

"""for i in range(a) : 
    print(i)
"""

"""var = 10  # 10 
for i in range(5):  # 4   ,5  
    for j in range(2, 3, 1): # 2,3
        if var%2 == 0:  # 18 % 2==0
            break
        var += 1  #  
        print(var)  
    var+=1  # 19  
else:
     var+=1  # 18 
print(var)
"""

"""A=0  # 0 
for i in range(4): #    3 
    if i%2==0:    # 3    % 2==0 
        pass
    else:
        continue
        break
    A+=1  # 2 
print(A)

"""

"""
A
AB
ABC
ABCD
ABCDE 
"""
# ord : ===> converts the characters of a string to their ASCII values 

"""
for i in range(1,6):
    for j in range(i):
        print(chr(ord('A')+j),end=" ")
    print()
"""

"""
    *        * * * * 
   * *        * * * 
  * * *        * * 
 * * * *        *
"""

"""
no :171 
Gross Pay, Annual Income and Income Tax Calculator

Write a Python program to calculate the gross pay, annual income, and income tax using the following data.

The gross pay consists of:
Basic Pay
House Rent Allowance (HRA)
Dearness Allowance (DA)
Other Allowances
Transport Allowance (TA)
Professional Tax
Employees’ Provident Fund (EPF) 

FORMULA  : Gross Pay = Basic Pay + HRA + DA + Other Allowances + TA - (Professional Tax + EPF)

| City Tier | Description | HRA             |
| --------- | ----------- | --------------- |
| 1         | Metro City  | 0.3 × Basic Pay |
| 2         | Tier 2 City | 0.2 × Basic Pay |
| 3         | Tier 3 City | 0.1 × Basic Pay |

Grade Levels and Pay Details: 

| Grade | Basic Pay (₹) | Other Allowances (₹) |
| :---- | ------------: | -------------------: |
| A     |         60000 |                 8000 |
| B     |         50000 |                 7000 |
| C     |         40000 |                 6000 |
| D     |         30000 |                 5000 |
| E     |         20000 |                 4000 |
| F     |         10000 |                 3000 | 

additional details : 

Additional Information:
Professional Tax = ₹200 (fixed per month)
Transport Allowance = ₹900 (fixed per month)
Provident Fund (EPF) = 0.11 × Basic Pay
Dearness Allowance (DA) = 0.5 × Basic Pay

Tasks:
1.Input grade level (A–F) and city type (1, 2, or 3).
2.Calculate Gross Pay for one month.
3.Calculate Annual Pay = Gross Pay × 12.
4.Compute Income Tax using the following slabs (as per FY 2022–23):

|     Annual Income (₹) | Tax Rate |
| --------------------: | -------: |
|        Up to 2,50,000 |       0% |
|   2,50,001 – 5,00,000 |       5% |
|   5,00,001 – 7,50,000 |      10% |
|  7,50,001 – 10,00,000 |      15% |
| 10,00,001 – 12,50,000 |      20% |
| 12,50,001 – 15,00,000 |      25% |
|       Above 15,00,000 |      30% |

output : 

Enter the grade level (A, B, C, D, E, or F): A
Enter the city (1 for metro, 2 for tier 2, 3 for tier 3): 1
Gross Pay of employee is: 110100.0
Annual Income of employee is: 1321200.0
Income Tax to be paid by employee is: 142800.0

"""
"""
number = 123 
sum = 1+2+3 =6 

"""

"""n=int(input("enter the number  : "))  # 1024
n1=int(input("enter the number  : "))  # 2
n2=int(input("enter the number  : "))  # 3

total_sum = n + n1 + n2


if n == n1 and n1 == n2:
    result =total_sum *3 
    print(result)
else :
    print(total_sum)
    
"""    

"""
happy number  : 

13 :  1*1 = 1 3*3 = 9   ==> sum = 1 + 9 = 10  ==> 1 *1 =1  0 * 0 =0  sum =1+0 =1 

4 :  
"""
# happy number :
"""
def happyNumber(n):  # 13 
    rem = sum = 0   #  rem = 0 sum =0 
    while True:            
        rem = n % 10   # rem  = 10 %10 =1  
        sum = sum + (rem**2)  #  sum =1   
        n = n // 10    # n  = 10//10 =0  
        if(sum==1 and n ==0):   
            print("Happy Number")
            break
        elif(sum==4 and n==0):
            print("Not a Happy Number")
            break
        if n==0:   # 
            n=sum   # n= 10
            sum=0   # sum =0 

n = int(input("Enter a number: "))  #13
n1 =int(intput("Enter a number: "))  #4

for i in range(n,n1+1):
    print(i)
happyNumber(n)
"""
"""a=10 
b=12 
c =14 
print(a,b,c)
"""
"""
for j in range(-1  ,-10 ,-1  ) :
    print(j)
"""
#          -10      -3 -2 -1 0 1 2 3 4 5 

"""
*               * 
* *           * *  
* * *       * * *
* * * *   * * * *
* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *
"""
"""a=1 
b=7
  
for i in range(1,6):    # 1 
    for j in range(0,i):   # 0,1 
        print("*",end="")
    for k in range(a,9):  # 1,9
        print(" ",end="")  # 
    for l in range(0,i):  # 0 ,1 
        print("*",end="")
    a=a+2   # a=3
    print()
for i in range(1,5):
    for j in range(i,5) :
        print("*",end="")
    for k in range(b,9):
        print(" ",end="")
    for l in range(i,5):
        print("*",end="")
    b=b-2 
    print()  
"""    

# que  : 181 :PB 
"""
num =int(input("enter the number  : "))  # 2
for i in range(100000 , 1000000)  :# all 6  digits  number  
    mul =1   # 111112  = 1*1*1*1*1*2 =2 
    temp =i 
    while temp >0 :
        r = temp %10   # r=0 
        mul = mul *r
        temp = temp //10 
    if mul ==num :
        print(i) 
"""

# PB  : 179 : 
"""
Write a python program that prompts the user to enter numbers and stops only when the use enter “QUIT” . After this 
print sum  and average of the numbers, minimum and maximum number from given numbers entered by user.
 Note: you are not allowed to use any built in structures like, list ,tuple etc. or any  builtin function like min, max  etc.
 For 
 Example:  Input:  4,1,5,”QUIT”
 Output:
 Sum=10
 Average=3.333
 Minimum number=1
 Maximum number=5
 """
 
"""count =0 
sum =0 
min_num =None 
max_num = None 

while True :
    n=input("enter the  number  :")  # 1 2 3 4  ==>  store in string  
    if n=="QUIT" or n=="quit" :
        break
    num = int(n)   # num = 2 
    sum = sum + num   # sum = 0 +1 =1 +2 =3  
    count +=1 
    
    if min_num == None or num < min_num :
        min_num=num
    if max_num == None or num > max_num :
        max_num=num
if count >0 : 
    print("Sum=",sum)
    print("Average=",sum/count) 
    print("Minimum number=",min_num)
    print("Maximum number=",max_num)
"""

"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
 The greatest common divisor (GCD) of two nonzero integers a and b is the greatest positive integer d such that d is a 
divisor of both a and b; that is, there are integers e and f such that a = de and b = df, and d is the largest such integer. The 
GCD of a and b is generally denoted gcd(a, b). 
For example, the greatest common factor of 15 and 10 is 5, since both the numbers can be divided by 5

"""
"""a= int(input("enter the number  : "))  # 15
b = int(input("enter the number  : "))  # 10

if a>0 and b > 0 :  #  5   and  0 > 0  
    while b !=0 :   # 5 ! =0 
        
        temp =b   # temp =5 
        b = a % b   # b = 10 % 5   = 0  
        a= temp  # a =5  
    print("GCD :",a)  # 5
else :
    print("GCD :",0)  # 0
"""
"""
 Ask the user to enter 10 test scores. Write a program to do the following:
 a)If user enters score greater than 100, then give warning to user that entered score is more than 100 and take that 
 input again from user.  b)Print out the highest and lowest scores.
  c)Print out the average of the scores.  d)Print out the second largest score.
 e)Drop the two lowest scores and print out the average of the rest of them.
 Note: Use of Python Data structures like string, list, tuple etc. and their inbuilt function is not allowed.
 For Ex.
 If Input is like following:
 Enter Test Score: 80
 Enter Test Score: 65
 Enter Test Score: 98
 Enter Test Score: 70
 Enter Test Score: 93
 Enter Test Score: 130
 Entered score is more than hundred, so enter again
 Enter Test Score: 95
 Enter Test Score: 50
 Enter Test Score: 40
 Enter Test Score: 75
 Enter Test Score: 72
 Output should be:
 Highest Score is: 98
 Lowest Score is: 40
 Average Test Score is: 73.8
 Second Largest Score is: 95
 Average after dropping the two lowest scores: 81.0
 """
 