Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # This is continution on 02/27/2026
>>> #to checck multiple condtions we can use if elif
>>> dtype=input("Please enter a data type ")
Please enter a data type 
>>> if dtype=="list":
...     print("List is muutable")
... elif dtype=="tuple":
...     print("Tuple is Immutbale")
... elif dtype=="set":
...     print("set is mutable")
... elif dtype=="dict":
...     print("dict is Mutable")
... else:
...     print("Please enter a valid data type")
... 
...     
Please enter a valid data type
>>> list
<class 'list'>
>>> List
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    List
NameError: name 'List' is not defined. Did you mean: 'list'?
>>> Please enter a valid data type
SyntaxError: invalid syntax
>>> List
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    List
NameError: name 'List' is not defined. Did you mean: 'list'?
