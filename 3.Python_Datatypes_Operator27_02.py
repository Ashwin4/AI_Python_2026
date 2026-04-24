Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This is for AI Class # 3 02/26/2026
##Set##
#######
#it starts with {}
#it does not allow duplicates
#IT does not have order
#no indexing
#It is mutable that is changeble
#It allows all types of data.

s={}
type(s)
<class 'dict'>
#Here dict also have the {} only.
#so here the preference was given to dict only.
#So we cant get empty set here.
#To get the empty set we need to apply typecasting function set()

s=set()
type(s)
<class 'set'>
s
set()
type(s)
<class 'set'>
s={34,23.33,"AI"}
s
{34, 'AI', 23.33}
s
{34, 'AI', 23.33}
s={2,2,34,11,11,12,"AI",444,333,222,111,444,111}
s
{2, 'AI', 34, 11, 12, 333, 111, 444, 222}
s
{2, 'AI', 34, 11, 12, 333, 111, 444, 222}

s[0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable

#Mutable we can add elements by using add() remove by remove()
s.add(33)
s
{33, 2, 'AI', 34, 11, 12, 333, 111, 444, 222}
s.add(231)
s
{33, 2, 'AI', 34, 231, 11, 12, 333, 111, 444, 222}
s.remove(231)
s
{33, 2, 'AI', 34, 11, 12, 333, 111, 444, 222}
#####################################################
####dict############
#--------------------
#it also starts with {}
#It have structure of {key:value,key:value,key:value,.....}
#Here keys are not duplicates..if we take as duplicate old value will be replaced by new value
#Duplicate values are allowed
#It is Mutable

d={}
type(d)
<class 'dict'>
d={101:"AI",102:"ML",103:"DL","GEN AI":"Agentic AI"}
d
{101: 'AI', 102: 'ML', 103: 'DL', 'GEN AI': 'Agentic AI'}

#how to add elements to that
#dict[key]=value

d[104]="Cloud"
d
{101: 'AI', 102: 'ML', 103: 'DL', 'GEN AI': 'Agentic AI', 104: 'Cloud'}

d[101]="Bigdata"
d
{101: 'Bigdata', 102: 'ML', 103: 'DL', 'GEN AI': 'Agentic AI', 104: 'Cloud'}

d[105]="ML"
d
{101: 'Bigdata', 102: 'ML', 103: 'DL', 'GEN AI': 'Agentic AI', 104: 'Cloud', 105: 'ML'}

#####################################################################
###range()-->we can call it as collection related datatype or a function
##collection of nos
#It has diff cases
#Case 1:range(n)-->It starts with 0 and ends with end-1
range(10)
range(0, 10)
r=range(10)
r
range(0, 10)
r[0]
0
r[1]
1
r[2]
2
#To see the elements in the given range we can take help of Iterative statements that is for here
#for-->for each variable in the given sequence i want some apply some functionality to each element

for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i is in range(100)
SyntaxError: invalid syntax
for i in range(100):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
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
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99

#case 2:range(start,end)
for i in range(20,30):
    print(i)

    
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

#case 3:range(start,end,step)#here step means it can be positive or negative

for i in range(30,40,2:
               
SyntaxError: incomplete input
print(i)
               
29
for i in range(30,40,2):
    print(i)

               
30
32
34
36
38
for i in range(60,40,-2):
    print(i)

               
60
58
56
54
52
50
48
46
44
42
for i in range(40,60,-2):
    print(i)

               
# Nothing will print because range is reverse 40 and 60 is higher than 40?
               
for i in range(42,60,2)
               
SyntaxError: incomplete input
for i in range(42,60,2):
    print(i)

               
42
44
46
48
50
52
54
56
58


#Operators
               
#-----------
               
#Symbols are grp of symbols..to do some operations on operands
               
#symbols means->+,-,/,<,>,=,*........
               
#Operands means inputs or values that we pass to operator
               

3+4
               
7
#+ is operator
               
 #3,4 are operands
               
#1.Arthemetic Operator:+,-,*,/,//,%,**
               
20/2
               
10.0
20//2
               
10
5/2
               
2.5
5//2
               
2
#% Modulus operator--it takes only remainder
               
10%2
               
0
10%3
               
1
100%9
               
1

3**2
               
9
9**3
               
729

#2.Relational:To check some condtions we can use
...                
>>> #<,>,<=,>=,==,!=..
...                
>>> 20<30
...                
True
>>> 45<=23
...                
False
>>> 44==34
...                
False
>>> 44!=44
...                
False
>>> 
>>> s="python"
...                
>>> s1="ai"
...                
>>> s>s1
...                
True
>>> #In the backend it checks ASCII value of each chracter..
...                
>>> #These are values we have 0 to 125
...                
>>> #how to check we have ord(),chr() these two predefined we can check those values
...                
>>> ord('p')
...                
112
>>> ord('a')
...                
97
>>> 112>97
...                
True
>>> #HEre it checks the first chracter ASCII value den compare..if both are same den only it go n check second chracter
...                
>>> chr(97)
...                
'a'
>>> chr(65)
...                
'A'
>>> chr(121)
...                
'y'
>>> chr(5)
...                
'\x05'
>>> chr(27)
...                
'\x1b'
>>> chr(56)
...                
'8'
