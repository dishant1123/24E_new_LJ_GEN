# opps : 
"""
class :

object : 

access modifier : 

1. public : accessible from anywhere
2. private : with in the same class
3. protected : with in the same class and its subclasses (inheritance)
"""

# ex :1  public : 
"""
class person :
    name =input("enter your name : ")
    age=int(input("enter your age : "))
    
    def show(self):  # self ==> keyword  ==>current object  ==> data member access 
        print("name is : ",self.name)
        print("age is : ",self.age)

p=person() 
# print("name is : ",p.name)
# print("age is : ",p.age)
p.show()
p.name ="het"
p.age=21
p.show()
"""

# ex :2 private : 

"""class student : 
    __name ="rishi"
    __age =21 
    
    def __show(self):
        print("name is : ",self.__name)
        print("age is : ",self.__age)
    
    def display(self):
        self.__show()
s=student()
# print("name is : ",s.__name)  # not  accessible  outside the  class bcz of  private . 
# print("age is : ",s.__age)
# s.show()
s.__name ="het"
s.__age=21
# s.show()
s.display()
"""

# ex :3 protected :

"""class vehicle : 
    _name ="car"
    _model ="toyota"

class car(vehicle):
    def show(self):
        print("name is : ",self._name)
        print("model is : ",self._model)

v=vehicle()
# print("name is : ",v._name)
# print("model is : ",v._model)
c=car()
c.show()
"""

# constructor  :  automatically called when an object is created
"""
1.defualt constructor
2.parameterized constructor
3.non parameterized constructor
4. constructor overload
"""
# 1. default constructor
"""
class student : 
    def __init__(self):  # def function  ==> __init__ ==> special method / constructor
        print("default constructor")

s=student()
"""

# 2. non parameterized constructor

"""class student : 
    def __init__(self):
        self.name ="yash"
        self.age=21
        print("non parameterized constructor")
    
    def show(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
s=student()
print(s.name)
print(s.age)
s.show()
"""

# 3. parameterized constructor

"""class vehicle : 
    def __init__(self,name):
        self.name =name 
        self.model ="audi"
        print("parameterized constructor")
        
v=vehicle("car")
print("name is  : ",v.name)
print("model is : ",v.model)
"""

# 4 : constructor overload

"""class student : 
    
    def __init__(self):
        self.name ="yash"
        self.age=21
        print("student constructor ==>non parameterized")
        
    def __init__(self, name, age):
        self.name =name
        self.age=age
        print("student constructor ==>parameterized")
    
    def __init__(self):
        print("student constructor ==>default")
        
        
# s=student("yash",21)
# print(s.name)
# print(s.age)
s=student()
"""

# inheritance  : 

"""
single  inheritance  : 
    ex : class student  : 
        class teacher (student) 
        
multiple  : 
    ex : class a 
         class b 
        class c(a,b) 

multi level inheritance :
    ex : class a 
         class b(a)    ==> b ==>a 
        class c(b)   ==> c ==> a,b 
         
hirechy inheritance : multiple derived class can inherit  from  same base class . 
    ex : class a 
         class b(a)
         class c(a)

hybrid inheritance : it is  combination  of  more than one  inheritance. 
generally it combination  of  multiple  and  multi level. 

    ex : class a 
         class b(a)
         class c(a)
         class d(b,c)

"""
# ex : 

'''class student : 
    """
    def __init__(self,name,age):
        self.name =name 
        self.age=age
    """
    def __init__(self):
        self.name = "yash"
        self.age =21 
            
class teacher(student) :
    # def __init__(self, name, age,subject):
    #     # student.__init__(self,name,age)   # base class constructor called 
    #     super().__init__(name,age)
    #     self.subject=subject
        
    def __init__(self):
        self.subject ="maths"
        # super().__init__()
        # student.__init__(self)
        
    def show(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
        print("subject is : ",self.subject)
        
t=teacher()
t.show()
'''

# encapsulation  : 
"""
1.get method  : print private variable 
2.set method  :  private  variable can modify using set method. 
"""
class student : 
    def __init__(self): 
        self.__name ="yash" 
        self.__age=21
        
    def get_name(self):
        return self.__name 
    
    def get_age(self):
        return self.__age
    
    def set_name(self,n_name):
        self.__name=n_name
        
s=student()
print("before using set method .")
print("name is : ",s.get_name())
print("age is : ",s.get_age())

print("after using set method .")
s.set_name("het")
print("name is : ",s.get_name())
print("age is : ",s.get_age())