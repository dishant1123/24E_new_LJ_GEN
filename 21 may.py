import datetime  

# now  =  datetime.datetime.now()
# print(now)

# today =datetime.datetime.today()
# print(today)

# a =datetime.datetime(2025,5,21,19,45,14,1477)
# print(a)
# print(a.strftime("%d-%m-%y  %H: %M: %S"))

# s =datetime.date(2025,5,21)
# print(s)

# print(datetime.time())

# from datetime import time as t 
# print(datetime.datetime.ctime())

import time  

"""print(time.ctime())
print(time.asctime())

print(time.localtime())

print(time.gmtime())
"""

"""for i in range(10):
    time.sleep(1)
    print(i)

"""    

from datetime  import timedelta 

"""now = datetime.datetime.now()
future = now + timedelta(days=5)
print(future)
"""
# sub  time  : 

"""now = datetime.datetime.now()
past = now -timedelta(hours=2)
print(past)
"""
# diff in date time  : 

"""d1 =datetime.date(2025,5,25)
d2 =datetime.date(2023,4,30)

delta =d1-d2
print("diffrence :",delta)
print("diffrence in days :",delta.days)
print("diffrence in time :",delta.total_seconds)

"""
# calender : 

"""
import calendar 

print(calendar.calendar(2025))
"""

"""import datetime   # date  , time , datetime 

a = datetime.datetime.now()
print(a)

#26 / 5 /2025  6 : 30 :45 
print(a.strftime("%d-%m-%y  %H:%M:%S"))

b=datetime.datetime.today()
print(b)

c=datetime.datetime(2025,5,25)
print(c)

print(datetime.date(2025,6,30))

import time 

j=time.ctime()
print(j)

s=time.localtime()
print(s)
"""
"""for i in range(10):
    print(i)
    time.sleep(1)
"""
# import math 

# print(math.factorial(5))

"""from datetime import timedelta

today=datetime.datetime.now()
future = today + timedelta(days=5,seconds=45,minutes=60)
print(future)

s=datetime.datetime.now()
"""