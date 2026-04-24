Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This is from AI Recording Session #14
#Imp functions and methods in STring##
s="python"
type(s)
<class 'str'>
s.lower()
'python'
s.upper()
'PYTHON'
s=" python"
s.strip()
'python'
a=" py thon"
a
' py thon'
# It removes the spaces from begining and end
s="  py thon "
s.stripe(s)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.stripe(s)
AttributeError: 'str' object has no attribute 'stripe'. Did you mean: 'strip'?
s.strip(s)
''
s=" py thon  "
s.strip(s)
''
s.strip()
'py thon'
s.find("y")
2
s
' py thon  '
#Finds the position of substring
s.find("p")
1
s="python"
s.count('p')
1
#Count the occurence
s="AABBAAABBBCCCCAAAAABBBBB"
s,count("A")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s,count("A")
NameError: name 'count' is not defined. Did you mean: 'round'?
s.count("A")
10
s.count("AA")
4
s.count("AAA")
2
s="I love ml"
s.replace("ml","dl")
'I love dl'
#Replace the part of string

len(s)
9

s="python"
#Output as: Python
s.replace("p","P")
'Python'
s.upper('n')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.upper('n')
TypeError: str.upper() takes no arguments (1 given)
s.upper()
'PYTHON'
s[5]
'n'
#Output as:PythoN
s.replace("p","P")
'Python'
s[5].upper()
'N'
s[0].upper()
'P'
s[0].upper()+"yth"+s[-1].upper()
'PythN'
s="machine learning"
s[0].upper()+"yth"+s[-1].upper()
'MythG'
# To use correct coding use this
s[0].upper()+s[1:-2].lower()+s[-1].upper()
'Machine learniG'
# This code will work for all lenths
s="deeplearning"
s[0].upper+s[1:-2].lower()+s[-1].upper
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s[0].upper+s[1:-2].lower()+s[-1].upper
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'str'
s[0].upper+s[1:-2].lower()+s[-1].upper()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s[0].upper+s[1:-2].lower()+s[-1].upper()
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'str'
s[0].upper()+s[1:-2].lower()+s[-1].upper()
'DeeplearniG'
s[0].upper()+s[1:-1].lower()+s[-1].upper()
'DeeplearninG'
# This is correct because it should be -1 not -2
s="Machinelearning"
s[0].upper()+s[1:-1].lower()+s[-1].upper()
'MachinelearninG'
s.title()
'Machinelearning'
s="i love ml"
s.title()
'I Love Ml'
s.capitalize()
'I love ml'
# This will do only 1st one character as capilalize
s
'i love ml'
s.split()
['i', 'love', 'ml']
#split():It splits the string...the default parameter is space
#syntax is-->string.split(parameter)
s.split(":")
['i love ml']
s="30-12-1999"
s.split("-")
['30', '12', '1999']

#join-->add the grp of strings together
l=["ml","dl","AI"]
#syntax is -->seperator.join(list)
" ".join(l)
'ml dl AI'

'30-12-1999'
'30-12-1999'
s
'30-12-1999'
s.isalpha()
False
s.isdigit()
False
s="890"
s.isdigit()
True
s="Abc"
s.alpha()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
s.isalpha()
True
s="AI234"
s.isalphanum()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    s.isalphanum()
AttributeError: 'str' object has no attribute 'isalphanum'. Did you mean: 'isalnum'?
s.isalnum()
True

#Imp methods and func in LIst##
################################
l=[3,4,5,6]
l,append(44)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    l,append(44)
NameError: name 'append' is not defined
l.append(44)
l
[3, 4, 5, 6, 44]
l.index(3)
0
#it gives the index number
l.insert(2,444)
l
[3, 4, 444, 5, 6, 44]
l.insert(2,444)
l
[3, 4, 444, 444, 5, 6, 44]
l.insert(99,999)
l
[3, 4, 444, 444, 5, 6, 44, 999]
l.insert(-100,100)
l
[100, 3, 4, 444, 444, 5, 6, 44, 999]
# Extend will add into list
l.extend([333,444])
l
[100, 3, 4, 444, 444, 5, 6, 44, 999, 333, 444]
l.append([666, 777])
l
[100, 3, 4, 444, 444, 5, 6, 44, 999, 333, 444, [666, 777]]
# Append as nested list
# If we add () instead of [] it will add as tuple
l.append((666, 777))
l
[100, 3, 4, 444, 444, 5, 6, 44, 999, 333, 444, [666, 777], (666, 777)]
# We can finf element as Indix number
l[10]
444
l[11]
[666, 777]
l(12)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    l(12)
TypeError: 'list' object is not callable
l[12]
(666, 777)
# We can use two index if we lind only one from list
l[11][0]
666
# Remove will remove element
l.remove(100)
l
[3, 4, 444, 444, 5, 6, 44, 999, 333, 444, [666, 777], (666, 777)]
# The 1st 100 is removed
l.remove(3)
l
[4, 444, 444, 5, 6, 44, 999, 333, 444, [666, 777], (666, 777)]
# Pop will remove last element
l'pop()
SyntaxError: incomplete input
l.pop()
(666, 777)
l
[4, 444, 444, 5, 6, 44, 999, 333, 444, [666, 777]]
# Reverse order
l.reverse()
l
[[666, 777], 444, 333, 999, 44, 6, 5, 444, 444, 4]
# Sort will sort the list in acending order
l.sort()
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'int' and 'list'
l.sort()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'int' and 'list'
l
[[666, 777], 444, 333, 999, 44, 6, 5, 444, 444, 4]
l.sort()
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'int' and 'list'
l'remove([666,777])
SyntaxError: incomplete input
l.remove([666,777])
l
[444, 333, 999, 44, 6, 5, 444, 444, 4]
l'sort()
SyntaxError: incomplete input
l.sort()
l
[4, 5, 6, 44, 333, 444, 444, 444, 999]
# If need desending than user reverse
l.reverse()
l
[999, 444, 444, 444, 333, 44, 6, 5, 4]
l=[34,12,1,90]
>>> l.sort(reverse=False)
>>> l
[1, 12, 34, 90]
>>> l.sort()
>>> l
[1, 12, 34, 90]
>>> l.sort(reverse=True)
>>> l
[90, 34, 12, 1]
>>> 
>>> #list comprehension
>>> #easy and concise way to create the list
>>> #syntax is--[expression for loop if condition(optional)]
>>> 
>>> l=[]
>>> for 1 in range(1,100):
...     
SyntaxError: cannot assign to literal
>>> for i in range(1,101):
...     if i%2==0:
...         l.append(i)
... 
...         
>>> l
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> # This is printing all even number
>>> # Usee this as list comprehension
>>> l=[for i in range91,101) if i%2==0]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> l=[i for i in range(1,101) if i%2==0]
>>> l
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> # We use this list comprehension######
>>> l
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> # To print odd number
>>> l=[i for i in range(1,101) if i%2==1]
>>> l
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
