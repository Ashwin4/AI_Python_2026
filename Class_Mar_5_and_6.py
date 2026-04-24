"""

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



Methods:
--------
1.Instance  methods:
---------------------

Inside method implementation if we are using instance variables then such type methods
are called instance methods.

Inside declaration we have to pass self varibale.

2.Static methods:
=================
They are general utility methods.
Inside of these methods we wont use any instnace or class variables.
here wont provide self or cls
we can declare using @staticmethod decorator
we can access static method by using class name or object reference




3.Class methods
-----------------
Inside the method implementation if we are using only class variables(static variable)

we can declare class method by using @classmethod decorator

for class method we should provide cls variable at the of declaration.

cls variable will contains all class level information.

we can call classmethod by uisng classname or object reference variable.



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

class emp:
    designation="Data scientist"#static variable
    def __init__(self,name,location):#a special method-->construcutor
        self.name=name#instance variable
        self.location=location#isntance variable
    def show(self):#It is a method--Instance method
        print("TEch name is ",self.name)
        print("location is ",self.location)
        hq="Delhi"#local variable
        print("the headquarter situated at",hq)
    @classmethod
    def show_desig(cls):
        print("the designation of all employes are ",cls.designation)

    @staticmethod
    def salary(m1,m2):
        print("The total salary of two months is in usd dollars  ",m1+m2)

e=emp("AI","India")#Automatically the construcotr will be executed we no need to call when -->e
e1=emp("ML","USA")#automatically the const will be called-->e1
e2=emp("DL","Japan")

e.show()
e.salary(200,300)
e1.salary(100,200)
e2.salary(200,150)

emp.show_desig()


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
