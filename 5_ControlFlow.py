Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This is from 02/27/2026 AI Class #4
## Control Flow##
#The order it executes our code.By default python follow top to bottom approach.. but it controls the flow by make decisions,repeating the tasks and sometime skip the code....

#Types of control flow
#1.Conditional statements--if,if else,if elif
#2.Iterative statements
#Iterative means -->for,while
#3.Transfer statements--break ,continue

#1.Conditional--
#syntax:
#if condtion:
#   stmt1

a=20
if a<30:
    print("Hellow ai")

    
Hellow ai
a=50
if a<30:
    print("hellow ai")

    
if a<30:
    print("hellow")
else:
    print("AI")

    
AI
# =============== RESTART: C:/Users/kumar/Desktop/7pm_Controlflow.py ===============
Please enter a data type list
SyntaxError: invalid syntax
#Please enter a data type list
# List is muutable
Please enter a data type tuple
SyntaxError: invalid syntax
# Please enter a data type tuple
# Tuple is Immutbale
# Please enter a data type int
# Please enter a valid data type

#2.Iterative statemtns--for ,while
#while-->by checking some condtion it execute stmts repearedly untill unless the condtio become false
>>> a=20
>>> while a<-30:
...     print(a)
...     a=a+1
... 
...     
>>> while a<=30:
...     print(a)
...     a=a+1
... 
...     
20
21
22
23
24
25
26
27
28
29
30
>>> 
>>> #3.Trasfer control--break,continue
>>> #break--simply by checking the condition coming out of the loop
>>> a=30
>>> while a<40:
...     if a==35:
...         break
...     print(a)
...     a=a+1
... 
...     
30
31
32
33
34
>>> 
>>> #continue--simply skip the current iteration by checking some condtion only then proceed further iteration
>>> 
>>> a=30
>>> while a<=40:
...     a=a+1
...     if a==35:
...         continue
...     print(a)
... 
...     
31
32
33
34
36
37
38
39
40
41
