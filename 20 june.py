# hybrid inheritance  : 
"""
class a :  #base class 
    name
class b (a) :   #deri 1 
     age 
class c :(a)    #deri 2 
    salary 
class d (b,c) :
     address  ,name  age  salary 

"""

"""class vehicle: 
    def __init__(self,name):
        self.name =name 

class car (vehicle):
    def __init__(self,color):
        self.color = color

class bike (vehicle):
    def __init__(self,speed):
        self.speed=speed

class truck(car , bike):
    def __init__(self, color,speed,capacity):
        car.__init__(self,color)
        bike.__init__(self,speed)
        self.capacity =capacity
    def  display(self):
        # print(self.name)
        print(self.color)
        print(self.speed)
        print(self.capacity)

t=truck("black",150,4000)
t.display()
"""