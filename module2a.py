# This is from AI Session #10 03/04/2026
import module1
print(module1.x)
module1.add(3,4)
module1.product(5,6)

from module import add as a
a(4,3)
# If we use * everything will print
from module import *
add(4,3)
product(8,4)
print(x)
"""
Module:
--------

A grp of functions,variables and classes saved into a file,which is nothing but a module

Every python file acts as a module


here module1 contains one variable and two functions

WE can say members of module.

if we want to use the members of this module in other program then we should import the module.

import modulename

-->We can access members by using module name
modulename.variable
modulename.function()

Renaming a module called as Module aliasing

import modulename as m

we can access memebers using alias name only 



from import:
-----------

we can import particular member module using from
the main advantage here is we can access them directly without using module name

member aliasing also possible


finding the members of the module:
----------------------------------

Python provides inbuilt function dir() it list out all members of current module
or a specified module

dir()-->It list out all members of current module

dir(modulename)-->It list out all members of specified module

For every module at the time of execution Python will add some special properties automatically

Ex:_builtins_,_doc_,_file_,_name_.....



"""
