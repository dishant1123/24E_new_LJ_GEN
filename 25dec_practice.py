"""
class object : 
"""

"""
class student  :
    # name ="saloni"
    # age =20  
    name=input("enter the  name  :")
    age=int(input("enter the age : "))
    def show(self): 
        print(self.name)
        print(self.age)
s=student()
print(s.name)
print(s.age)
s.show()
s.name="pinal"
s.age=21
s.show()
"""

# private  : 

"""class student :
    __name ="pinal"
    __age=20
    def __show(self):
        print("name is  :",self.__name)
        print("age is  :",self.__age)
    def display(self):
        self.__show()
s=student()
# print("name is  : ",s.__name)   # bcz of private not accessible outside the class .
# print("age is : ",s.__age)
# s.show()
s.__name="saumya"
s.__age=19
# s.show()
s.display()
"""
# protected :

"""class vehicle :
    _model ="audi Q-7"
    _speed =200
    
class car: 
    def show(self):
        print(self._model)
        print(self._speed)
c=car()
c.show()
c._model="bmw"
c._speed=250
c.show()
"""
# constructor  : 
"""
1. default  
2. parameter 
3. non parameter
"""
#1 :
"""class student : 
    def __init__(self):
        print("saloni , pinal ==> old LJ student")

s=student()
"""
#3 :
"""class studenet :
    def __init__(self):
        self.name ="saloni"
        self.age =19 
        print("LJ student")
    def show(self):
        print(self.name)
        print (self.age)
s=studenet()
s.show()
s.name="pinal"
s.age=20
s.show()
"""

#2 : 
"""
class employees: 
    def __init__(self,age,name="saumya"):
        self.name =name 
        self.age =age        
    def show(self):
        print(self.name)
        print (self.age)
e=employees()
e.show()
e1=employees("saloni",19)
e1.show()
"""        
        
# inheritance  : 
"""
1.  single inheritance
2.  multiple inheritance
3. multilevel inheritance
4. hybrid inheritance
5. hirechical 
"""

"""class test : 
    def __init__(self,x):
        self.x =x
    
    def change(self):
        self.x =self.x +1 

class test2(test):
    def __init__(self, y,z,x):
        self.y=y 
        self.z=z
        super().__init__(x)
    def change(self):
        # super().change()
        # self.x =self.x +2
        print("x :",self.x) 
        print("y :",self.y)
        print("z :",self.z)
    
 
t=test2(12,34,35)
t.change() 
"""

# multi level  :          multiple       hirechy :
"""
class a                   class a       class a 
 
class b(a) :              class b       class b(a)

class c(b)                class c(a,b)   class c (a) 
                                        
                                         class d(b,c)
    
""" 

"""class Demo:
    def che(self):
        return " Demo's check "  
    def display(self):
        print(self.che())

class Demo_Derived(Demo):
    def check(self):
        return " Derived's check "

Demo().display()
Demo_Derived().display()
"""

