Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This is for 02/26/2026 AI Class # 3
##Operators##
#3.Assignment operator: to assign a value we use = operator
#On top of this assignment operator we can apply some other operator den  we can it as compund assigment operator
a=20
a+=30 #a=a+30
a
50
a-=20
a
30

#4.Logical opearators--and , or ,not
#and-->both condtions becom True
#or ->At least one True
#not-->reverse condition

age=25
salary=50000
age>19 and salary>30000
True
True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True and True
True
>>> 
>>> not true
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> not True
False
>>> not Fauls
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    not Fauls
NameError: name 'Fauls' is not defined. Did you mean: 'False'?
>>> not False
True
>>> 
>>> #5.Membership operators
>>> #Used to check presnece in the sequence
>>> #in-->Present
>>> #not in -->Not present
>>> 
>>> i=[2,3,4]
>>> 3 in i
True
>>> 88 in i
False
>>> 90 not  in i
True
>>> 
>>> #6.Identity operators
>>> #Check the memory locations
>>> #is-->same object
>>> #is not-->diff object
... 
>>> l=[4,5,3]
>>> m=l
>>> n=[4,5,3]
>>> l is m
True
>>> 
>>> l is n
False
>>> 
>>> #7.Ternary operator--Condtional operator
>>> #syntax:-->True_value if condition else False_value
>>> 
>>> a=30
>>> b=40
>>> c=60 if a>b else 30
>>> c
30
