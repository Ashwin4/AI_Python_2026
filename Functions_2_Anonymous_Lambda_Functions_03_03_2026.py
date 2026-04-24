Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This from AI Class session 10
#Anonymous Functions or Lambda functions
#########################################
#Some times we can declare a function without any name such type of nameless funtions are called anonymous or lambda functions
#The main purpose of this is just for instant use.

#Normal functions :i want square of a number
def sqart
SyntaxError: incomplete input
# we have to define by using lambda keyword
# Syntax: lambda arguments:expression
s=lambda n:n*n
s(2)
4

#by using lambda we can write very concise code
#labbda fuctiobs internally returns expression value so we are not required to write any return stmts here,

# Sometimes we can pass functions as arguments to another functions, In such cases we lambda is the best choice

def f1(f2,a,b):
    pass

def f2():
    pass

def f2(a,b):
    return a+b

def f1(f2,x,y):
    pass

def f1(f2):
    f2()

    
def f2():
    print("f2 function")

    
f2()
f2 function
f1()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    f1()
TypeError: f1() missing 1 required positional argument: 'f2'
f1(f2)
f2 function
f1("ai")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    f1("ai")
  File "<pyshell#32>", line 2, in f1
    f2()
TypeError: 'str' object is not callable

# we can use lambda very commonly with filter(), map(), reduce() because these functions expect function as arguments

#filter(function, sequence)==> to filter the values from the given sequence based on some condition .. so that condition checking is done by function

# now with out lambda
# how to filter()

#A program to filter the even nos by using list
l=[5,6,7,8,9,12,13,14]

def isEven (x):
     if x%2==0:
         return True
     else:
         return False
 
     
 l
[5, 6, 7, 8, 9, 12, 13, 14]
>>> 
>>> l1-list(filter(isEven,l))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    l1-list(filter(isEven,l))
NameError: name 'l1' is not defined. Did you mean: 'f1'?
>>> l1-list(filter(isEven,l))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    l1-list(filter(isEven,l))
NameError: name 'l1' is not defined. Did you mean: 'f1'?
>>> l1-list(filter(isEven,l))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    l1-list(filter(isEven,l))
NameError: name 'l1' is not defined. Did you mean: 'f1'?
>>> l1=list(filter(isEven,l))
>>> l1
[6, 8, 12, 14]
>>> 
>>> #with lambda
>>> l
[5, 6, 7, 8, 9, 12, 13, 14]
>>> l2=list(filter(lambda a:a%2==0,l))
>>> l2
[6, 8, 12, 14]
>>> 
>>> #mao *function, sequence( == for every element present in the sequence apply some functionality and generate new element with required modifications..
>>> 
>>> l
[5, 6, 7, 8, 9, 12, 13, 14]
>>> l2=list(map(lambda x:x*2,l))
>>> l2
[10, 12, 14, 16, 18, 24, 26, 28]
>>> 
>>> l2=list(map(lambda x:x%2==0,l))
>>> l2
[False, True, False, True, False, True, False, True]
