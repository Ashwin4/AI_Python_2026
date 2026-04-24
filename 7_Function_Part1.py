Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# AI Class # 5 Monday 03/02/2026 Holi
#Functions#
###########
#when a grp stmts are keep on repeating its better to dont write everytime instead of that try to write as a single unit or block ang give name for that block..whenver u need simply call that block..a single/block call it as a Function

#Two types of funcitons
#1.Predefined or Built in functions-->they comes along with the python
#Ex:print(),input(),type(),id()...

#2 .User defined functions--Depedning upon application requirement the programmer write his own logic and develop function..

#syntax:

#def function_name(parameters):
#       stmt1
#       stmt2
#       return value

#here def and return are keywords
#def is mandatory
#return is optional
#parametrs--Inputs that we pass to functions
#parametrs also optional only but mostly we pass the inputs

def wish():
    print("hellow")

    
wish()
hellow
wish()
hellow
wish()
hellow

def wish(name):
    print("Hellow", name)

    
wish()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    wish()
TypeError: wish() missing 1 required positional argument: 'name'
wish("AI)
     
SyntaxError: incomplete input
wish("AI")
     
Hellow AI
wish("ml")
     
Hellow ml

#If a function contains parametrs,then at the time of calling compulsory we should provide values otherwise we will get error.

#return:function can take input values as parametrs and executes the logic within the block then returns output to the caller with return statement.
     
#return is optional only
     
#the default return value is None
     
#otherwise if u r returning means it can be that value
     

def add(a,b):
    print("the sum is  ", a_b:
          
SyntaxError: incomplete input
    print("the sum is  ", a+b)
          
SyntaxError: unexpected indent
    print("the sum is ",a+b)
          
SyntaxError: unexpected indent
        print("the sum is ",a+b)
          
SyntaxError: unexpected indent

add()
          
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    add()
NameError: name 'add' is not defined
add(3,6)
          
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    add(3,6)
NameError: name 'add' is not defined

def add(a+b):
    
SyntaxError: invalid syntax




def add(a,b):
    print("the sum is ",a+b)

    
add(5,6)
the sum is  11
r=add(4,3)
the sum is  7
r
print(r)
None

def(a,b):
    
SyntaxError: invalid syntax
def add(a,b):
    return a+b

add(4,5)
9
r=add(3,2)
r
5

def add(a,b):
    print("sum is ",a+b)
    return "AI"

add(2,3)
sum is  5
'AI'

def calc(b,b):
    add=a+b
    
SyntaxError: incomplete input
sub=a-b
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    sub=a-b
NameError: name 'a' is not defined
    sub=a-b
    
SyntaxError: unexpected indent
    sub=a-b
    
SyntaxError: unexpected indent
    sub=a-b
    
SyntaxError: unexpected indent
def calc(b,b):
    add=a+b
    
SyntaxError: incomplete input




def calc(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div

calc(3.4)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    calc(3.4)
TypeError: calc() missing 1 required positional argument: 'b'
cal(3,4)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    cal(3,4)
NameError: name 'cal' is not defined. Did you mean: 'calc'?
calc(3,4)
(7, -1, 12, 0.75)
#when u return multiple values the backend is tuple

#Types of arguments:
#-------------------
#there are 4 types of arguments we have
#1.Positional
#2.Keyword
#3.Default
#4.Variable length arguments
#5.Keyword variable length arguments

#positional arguments:
#----------------------
#there are the arguments we passes to function in corrrect postion order
def sub(a,b):
    print(a-b)

    
sub(100,200)
-100
sub(200,100)
100
#here order is imp

#Keyword:we can pass by parameter name

sub(a=100,b=200)
-100
sub(b=200,a=100)
-100

#Default-->sometiems we provide default values
def wish(name="AI"):
    print("hellow",name)

    
wish()
hellow AI
wish("ML")
hellow ML

#variable length arguments
#we have to decalre by using *
#here it takes 0 to any arguments it can take
#the backend of this is tuple

def f1(*n):
    print(n)
    print(type(n))

    
f1()
()
<class 'tuple'>
f1(2)
(2,)
<class 'tuple'>
f1(3,4)
(3, 4)
<class 'tuple'>
f1(4,5,6)
(4, 5, 6)
<class 'tuple'>

add(3,4,5):
    
SyntaxError: incomplete input
def add(a,b):
    return a+b

add(3,4,5)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    add(3,4,5)
TypeError: add() takes 2 positional arguments but 3 were given
def add(a,b,c):
    return a+b+c

def add(*n):
    total=0
    for i in n:
        total=total+1
    print("the sum is ",total)

    
add()
the sum is  0
add(3)
the sum is  1
add(3)
the sum is  1
add(3,4)
the sum is  2

def add(*n):
    total=0
    for i in n:
        total=total+i
    print("the sum is ",total)

    
add()
the sum is  0
add(3)
the sum is  3
add(4,5,6)
the sum is  15

add(2,3,5,1)
the sum is  11

>>> #we can call this is a *args
>>> #keyword variable length arguments:
>>> #we have declare by using **
>>> #here backend is dict
>>> 
>>> def f1(**N):
...     print(n)
... 
...     
>>> f1()
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    f1()
  File "<pyshell#186>", line 2, in f1
    print(n)
NameError: name 'n' is not defined. Did you mean: 'N'?
>>> 
>>> 
>>> def f1(**n)
SyntaxError: incomplete input
>>> 
>>> def f1(**N):
...     print(n)
... 
...     
>>> f1()
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    f1()
  File "<pyshell#194>", line 2, in f1
    print(n)
NameError: name 'n' is not defined. Did you mean: 'N'?
>>> 
>>> def f1(**n):
...     print(n)
... 
...     
>>> f1()
{}
>>> f2(20)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    f2(20)
NameError: name 'f2' is not defined. Did you mean: 'f1'?
>>> 
>>> f1(a=20)
{'a': 20}
>>> f1(a=30, b=40, c-09, "ai"=34)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 
>>> f1(a=20)
{'a': 20}
>>> f1(a=30, b=40, c=09, "ai"=34)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> f1(a=30, ai=34)
{'a': 30, 'ai': 34}
>>> f1(a="ai", b="ml")
{'a': 'ai', 'b': 'ml'}
>>> 
