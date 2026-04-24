Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=40
type(a)
<class 'int'>
type(b)
<class 'int'>
id(a)
140717464341528
id(b)
140717464342168
#int,float,string,bool
#fundamental data types
c=45.55
type(c)
<class 'float'>
int a =30
SyntaxError: invalid syntax
a=30
type(a)
<class 'int'>
#This IDLE Shell is REPL tool
#READ
#Evaluate

#loop

c="python"
c
'python'
type(c)
<class 'str'>

#str:anything we can take single or double quatation is called string
s="ai"
s='ml'
s1="34"
s4="55.66"
type(s4)
<class 'str'>
type(s1)
<class 'str'>

#bool--True or False
#to check some condtions we use diff operators here the output is bool
20<30
True
45==34
False
56!=22
True

#all fundamental data types are immutable
#once we create an object we cant do any changes in that objecct.Once u try to change a
#new object is craeted..this is what immutbale behaviour...
a=30
id(a)
140717464341848
a=a+1
a
31
id(a)
140717464341880

#Type casting:Converting one type other type
#int(),float(),str(),bool()
int(45.66)
45
int(True)
1
int(False)
0
int("si")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int("si")
ValueError: invalid literal for int() with base 10: 'si'
int("45.33")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int("45.33")
ValueError: invalid literal for int() with base 10: '45.33'
int("34")
34

float(34)
34.0
float(True)4
SyntaxError: incomplete input
float(True)
1.0
float(False)
0.0
float("ai")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    float("ai")
ValueError: could not convert string to float: 'ai'
float("34.44")
34.44
float("22")
22.0

#bool-->if it is 0 then it is False other wise True only
#if it is empty string then False otherwise True only

bool(34)
True
bool(34.66)
True
bool(0)
False
bool(0.0)
False
bool("ai")
True
bool("")
False

#str()-->it convert all types
str(34)
'34'
str(45.22)
'45.22'
str(True)
'True'
str('False')
'False'
str("")
''

##Collection related Data types##
#Representing a grp of elements as single entity.Ex:list,tuple,set,dict,range..
#list,tuple,set,dict-->Python Data structures

#List:
#list must starts with []
#it follows order
#it allow the duplicates
#it has indexing concept
#it allows hetrogeneous objects-->allow all types of data

#list is Mutable-->Changeble

l=[]
type[l]
type[[]]
type(l)
<class 'list'>
l=[34,23.55,34,34,23,23,"AI",True]
l
[34, 23.55, 34, 34, 23, 23, 'AI', True]
#list has indexing--how to check that?
#list[index_value]
l[0]
34
l[3]
34

l
[34, 23.55, 34, 34, 23, 23, 'AI', True]
#mutable means changeble-->when something added or removed on top of that
#so here we can add by using append() method
#we can remove by using remove()

l
[34, 23.55, 34, 34, 23, 23, 'AI', True]
l.append(29)#this will be added at end of the list
l
[34, 23.55, 34, 34, 23, 23, 'AI', True, 29]
l.append(999)
l
[34, 23.55, 34, 34, 23, 23, 'AI', True, 29, 999]
#here the method is function only.Why calling as method?-->method means it will work for only particular #class..here append is method it works only list class.

l.remove(34)
l
[23.55, 34, 34, 23, 23, 'AI', True, 29, 999]
l
[23.55, 34, 34, 23, 23, 'AI', True, 29, 999]
l.remove(2)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    l.remove(2)
ValueError: list.remove(x): x not in list
>>> l.remove([2])
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    l.remove([2])
ValueError: list.remove(x): x not in list
>>> 
>>> l
[23.55, 34, 34, 23, 23, 'AI', True, 29, 999]
>>> l.remove(34)
>>> l
[23.55, 34, 23, 23, 'AI', True, 29, 999]
>>> 
>>> l[1]=333
>>> l
[23.55, 333, 23, 23, 'AI', True, 29, 999]
>>> 
>>> #tuple
>>> #tuple starts with () but it is optional
>>> #it follows the order
>>> #it has indexing
>>> #it allow duplicates
>>> #it allows all type of data
>>> #it is Immutable
... 
>>> t=(34,44,22)
>>> t
(34, 44, 22)
>>> t[0]
34
>>> t=34,34,34,22
>>> t=()
>>> type(t)
<class 'tuple'>
>>> 
>>> t=(22)
>>> type(t)
<class 'int'>
>>> >>> t=(22,)
SyntaxError: invalid syntax
>>> t=(22,)
>>> type(t)
<class 'tuple'>
>>> t=55,66,77
>>> type(t)
<class 'tuple'>
>>> t="ai",True,45
>>> t.append(44)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    t.append(44)
AttributeError: 'tuple' object has no attribute 'append'
>>> t.remove(33)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    t.remove(33)
AttributeError: 'tuple' object has no attribute 'remove'
>>> t
('ai', True, 45)
