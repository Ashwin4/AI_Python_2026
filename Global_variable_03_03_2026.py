Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This is from AI Session-10
"""
Variables in functions##
1.Global --which we declare outside of the function are called global
these variables accesed in all functions of that module

local variable:we declare within the funciton
Outside function we cannot access

global keyword:
-----------------
To declare global varibales inside the function
to make global variable available to the funciton so that we can perform
required modifications


"""
'\nVariables in functions##\n1.Global --which we declare outside of the function are called global\nthese variables accesed in all functions of that module\n\nlocal variable:we declare within the funciton\nOutside function we cannot access\n\nglobal keyword:\n-----------------\nTo declare global varibales inside the function\nto make global variable available to the funciton so that we can perform\nrequired modifications\n\n\n'

a=30#global
>>> def f1():
...     global a
...     a=777
...     print(a)
...     b=40#local variable
...     print(b)
... def f2():
...     
SyntaxError: invalid syntax
>>> print(a)
30
>>> def f2():
...     print(a)
...     #print(b)
... 
...     
>>> f1()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    f1()
NameError: name 'f1' is not defined. Did you mean: 'f2'?
>>> f2()
30
>>> f1()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    f1()
NameError: name 'f1' is not defined. Did you mean: 'f2'?
>>> a=30#global
>>> def f1():
...     global a
...     a=777
...     print(a)
...     b=40#local varibale
...     print(b)
... 
...     
>>> f1()
777
40
>>> f1()
777
40
>>> F2()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    F2()
NameError: name 'F2' is not defined. Did you mean: 'f2'?
>>> def f2():
...     print(a)
...     #print(b)
... 
...     
>>> f1()
777
40
>>> f2()
777
