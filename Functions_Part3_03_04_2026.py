Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This is for AI Session # 11 03/04/2026
## Functions Part 3 ##
#reduce (function, sequesnce)-->Reduce the grp of elements into single element.
#this is actually present in module called functools we need to import it.
from functools import reduce
l=[3,4,2,6,7,8,9]
r=reduce(lambda x.y:x+y,l)
SyntaxError: invalid syntax
r=reduce(lambda x,y:x+y,l)
r
39
r=reduce(lambda x,y:x-y,l)
r
-33
r=reduce(lambda x,y:x*y,l)
r
72576
r=reduce(lambda x,y:x/y,l)
r
0.0001240079365079365

############################################################################
###Nested Functions#############################
################################################
#A function within the function is called nested function.
def outer():
    print("outer function")
    def inner():
        print("Inner execution")
    print("Outer calling inner")
    inner()

    
inner()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    inner()
NameError: name 'inner' is not defined. Did you mean: 'iter'?
outer()
outer function
Outer calling inner
Inner execution

#A function can return another function
def outer():
    print("outer function")
    def inner():
        print("Inner execution")
    print("Outer calling inner")
    return inner

    
outer()
outer function
Outer calling inner
<function outer.<locals>.inner at 0x000001AFFD0D99E0>
# This will print only function location
# Now let store in r
r=outer()
outer function
Outer calling inner
#Let's print r value
r
<function outer.<locals>.inner at 0x000001AFFD0D9A80>
type(r)
<class 'function'>
# So to execute we needs to enter as function
r()
Inner execution
def outer():
    print("outer function")
    def inner():
        print("Inner execution")
    print("Outer calling inner")
    return inner

def outer():
    print("outer function")
    def inner():
        print("Inner execution")
    print("Outer calling inner")
    return inner()

outer()
outer function
Outer calling inner
Inner execution
r=outer()
outer function
Outer calling inner
Inner execution
#what is there in r?
#what is there in r?r
>>> print(r)
None
>>> 
>>> def outer():
...     print("outer function")
...     def inner():
...         print("Inner execution")
...         retun "AI"
...     print("Outer calling inner")
...     return inner
SyntaxError: invalid syntax
>>> def outer():
...     print("outer function")
...     def inner():
...         print("Inner execution")
...         return "AI"
...     print("Outer calling inner")
...     return inner
... 
>>> outer()
outer function
Outer calling inner
<function outer.<locals>.inner at 0x000001AFFD0CB060>
>>> def outer():
...     print("outer function")
...     def inner():
...         print("Inner execution")
...         return "AI"
...     print("Outer calling inner")
...     return inner ()
... 
>>> outer()
outer function
Outer calling inner
Inner execution
'AI'
>>> r=outer()
outer function
Outer calling inner
Inner execution
>>> r
'AI'
