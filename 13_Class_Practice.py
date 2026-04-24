"""
AI Session # 13 Pakages is a folder or directory it represent collection of python modules.
Package contains sub package also. Older version contains __init__.py file must be there even it is blank? But file must be there.

Class:
------

It is a Model/Plan/Blue print

WE can write a class to represent properties and actions of object.

Properties can be represented as Variables
Actions represented as Methods.

Here class contains both variables and methods.

By using class keyword

class classname:
    variables
    methods

Variables:
--------
1.Instance variables:
2.Static variables:
3.Local variables:

Methods:
--------
1.Instance  methods:
2.Static methods:
3.Class methods


Object:
-------
Physical existence of a class is object.
WE can create any no of objects.

Syntax to create object is -->
--------------------------------

reference_variable=classname()

constructor:
--------------
Special method in python
the name of constr is __init__(self)
const will be executed automatically at the time object creation
the main purpose of const is declare and intialize the instance variables
const take at least one argument--self
const is optional only but if dont provide any const pyhtohn will provide de fault const
Per object const will be executed only once.

self:
-----

self is a default variable which is always poiting the current object.

By using self we can access instance variables and instance methods.

self is the first parameter inside constructor.

self is the first parameter inside instance methods also.

self is not a keyword.

"""
"""
class emp:
    def __init__(self):#a special method-->construcutor
        self.name="AK"
        self.location="india"
    def show(self):#It is a method--Instance method
        print("name is ",self.name)
        print("location is ",self.location)

e=emp()# e is my reference variable. Automatically the constructor will be executed we no need to call when
e1=emp()# 2nd object, Autometically the const will be called -->e1
e2=emp()

e.show()
e1.show()

Variables:
--------

1.Instance variables:
---------------------

If the value of variable is varied from object to object.
For every object a seperate copy of instnce varibales will be created.

we can declare inside the constructor by using self variable
Inside instance method by using self
Outside of the class we can use by object reference variable.



2.Static variables:
------------------

If the values of a variable is not varied from object to object.
Such type variables we can declare within the class directly.

For total class one copy of static variable will be created and shared among all objects.

we can access static variables either by class name or object reference.

It is recommended to use class name.


3.Local variables:
-------------------

Sometimes to meet temporray requirements of programmer, we can declare variables inside 
a method directly.

they cannot acces frm outside of method.


# This is for recorded Session #13
class emp:
    designation="data Scientist"
    def __init__(self, name, location):#a special method-->construcutor
        self.name=name#instance variable
        self.location=location#isntance variable
    def show(self):#It is a method--Instance method
        print("Tech name is ",self.name)
        print("location is ",self.location)

e=emp("AI","India")# e is my reference variable. Automatically the constructor will be executed we no need to call when
e1=emp("ML","USA")# 2nd object, Autometically the const will be called -->e1
e2=emp("DL","Japan")

e.show()
e1.show()
e2.show()
print("The designation of all employee are ", emp.designation)
""" 

# this is for Local variable section
"""
3.Local variables:
-------------------

Sometimes to meet temporray requirements of programmer, we can declare variables inside 
a method directly.

they cannot acces frm outside of method.
# Add City = Dhlhi
"""
"""

class emp:
    designation="data Scientist"
    def __init__(self, name, location):#a special method-->construcutor
        self.name=name#instance variable
        self.location=location#isntance variable
    def show(self):#It is a method--Instance method
        print("Tech name is ",self.name)
        print("location is ",self.location)
        hq="Delhi" # Add local veriable here
        print("The headquarter situated at ",hq)

e=emp("AI","India")# e is my reference variable. Automatically the constructor will be executed we no need to call when
e1=emp("ML","USA")# 2nd object, Autometically the const will be called -->e1
e2=emp("DL","Japan")

e.show()
e1.show()
e2.show()
print("The designation of all employee are ", emp.designation)
"""

#This is Terminal Results
#2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Class_Practice.py
#Tech name is  AI
#location is  India
#The headquarter situated at  Delhi
#Tech name is  ML
#location is  USA
#The headquarter situated at  Delhi
#Tech name is  DL
#location is  Japan
#The headquarter situated at  Delhi
#The designation of all employee are  data Scientist
#PS C:\Users\jaiam\AppData\Local\Programs\Microsoft VS Code> 
# Now work on Methohs

"""

Methods:
--------
1.Instance  methods:
---------------------

Inside method implementation if we are using instance variables then such type methods
are called instance methods.

Inside declaration we have to pass self varibale.

Only this line in code
def show(self):#It is a method--Instance method



# Class method coding
3.Class methods
-----------------
Inside the method implementation if we are using only class variables(static variable)

we can declare class method by using @classmethod decorator

for class method we should provide cls variable at the of declaration.

cls variable will contains all class level information.

we can call classmethod by uisng classname or object reference variable.

"""
"""

class emp:
    designation="data Scientist"
    def __init__(self, name, location):#a special method-->construcutor
        self.name=name#instance variable
        self.location=location#isntance variable
    def show(self):#It is a method--Instance method
        print("Tech name is ",self.name)
        print("location is ",self.location)
        hq="Delhi" # Add local veriable here
        print("The headquarter situated at ",hq)
    @classmethod
    def show_desig(cls):
        print("The designation of all employes are ", cls.designation)


e=emp("AI","India")# e is my reference variable. Automatically the constructor will be executed we no need to call when
e1=emp("ML","USA")# 2nd object, Autometically the const will be called -->e1
e2=emp("DL","Japan")

e.show()
e1.show()
e2.show()
#We need to call now
emp.show_desig()
"""
"""
# This is terminal results
2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Class_Practice.py
Tech name is  AI
location is  India
The headquarter situated at  Delhi
Tech name is  ML
location is  USA
The headquarter situated at  Delhi
Tech name is  DL
location is  Japan
The headquarter situated at  Delhi
The designation of all employes are  data Scientist
"""
"""
2.Static methods:
=================
They are general utility methods.
Inside of these methods we wont use any instnace or class variables.
here wont provide self or cls
we can declare using @staticmethod decorator
we can access static method by using class name or object reference
"""
class emp:
    designation="Data Scientist"# This is a static variable
    def __init__(self, name, location):#a special method-->construcutor
        self.name=name#instance variable
        self.location=location#isntance variable
    def show(self):#It is a method--Instance method
        print("Tech name is ",self.name)
        print("location is ",self.location)
        hq="Delhi" # is local veriable here
        print("The headquarter situated at ",hq)
    @classmethod
    def show_desig(cls):
        print("The designation of all employes are ", cls.designation)

#Static Method
    @staticmethod
    def salary(m1,m2):
        print("The total salary of two months is in usd dollers",m1+m2)

e=emp("AI","India")# e is my reference variable. Automatically the constructor will be executed we no need to call when
e1=emp("ML","USA")# 2nd object, Autometically the const will be called -->e1
e2=emp("DL","Japan")

# Now we have to call for each employee
e.show()
e.salary(200,300)
e1.salary(100,200)
e2.salary(200,150)
#We need to call now
emp.show_desig()
"""
This is a terminal results
2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Class_Practice.py
Tech name is  AI
location is  India
The headquarter situated at  Delhi
The total salary of two months is in usd dollers 500
The total salary of two months is in usd dollers 300
The total salary of two months is in usd dollers 350
The designation of all employes are  Data Scientist
PS C:\Users\jaiam\AppData\Local\Programs\Microsoft VS Code
"""
"""

Assigmnet:
----------
welcome to AI bank

enter ur name: 
d-Deposit
w-withdraw
e-exit


choose your option: d
Enter the amount: 10000
Balance after deposit : 20000

choose option--w
enter the amount: 5000
balance after withdraw: 10000

choose option: e

exit


"""