Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This is AI Session # 15 Func and methods in Tuple
## Imp func and methods in Tuple##
##################################

t=2,3,5
type(t)
<class 'tuple'>
len(t)
3
t.count(2)
1
t.index(2)
0
t.append(33)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t.append(33)
AttributeError: 'tuple' object has no attribute 'append'
t.remove(2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t.remove(2)
AttributeError: 'tuple' object has no attribute 'remove'
#because of immutable behaviour we dont have much fun n methods

#Tuple comprehension: Is that possible or Not? --Not
#Due to that immutable we cant create a tuple comprehension.

t=(i for i in range(10))
t
<generator object <genexpr> at 0x00000220273A3E80>
# It is generator not a tuple

#Imp functions in set#
######################
s={3,4,4,3,56,77,23,12}
s
{3, 4, 23, 56, 12, 77}
s.add(333)
s
{333, 3, 4, 23, 56, 12, 77}
s.remove(3)
s
{333, 4, 23, 56, 12, 77}
# added 333 and removed 3
len(s)
6
s.count(4)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.count(4)
AttributeError: 'set' object has no attribute 'count'
s
{333, 4, 23, 56, 12, 77}
s={1,2,3,4,5,6,7}
s1={2,3,5,8,9}
s.union(s1)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
# Combaine two set but filtering duplicate
s.intersection(s1)
{2, 3, 5}
# will print ony match in two set
# Common on two set
s.difference(s1)
{1, 4, 6, 7}
# Not common on both set
# s={1,2,3,4,5,6,7}
# s1={2,3,5,8,9}
# This is on 1st set but not in second set
# set comprehension possible?
# Yes
s={i for i in range(1,100) if i%3==0}
s
{3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99}

s.update(s1) # This will add all values from s1 to s
# s = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99}
# s1 = {2,3,5,8,9}
s
{2, 3, 5, 6, 8, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99}
# Another example
s={3,4,5}
s1
{2, 3, 5, 8, 9}
s.update(s1)
s
{2, 3, 4, 5, 8, 9}
# We can add list also
s.update([4,5,3])
s
{2, 3, 4, 5, 8, 9}
s.remove(3)
s
{2, 4, 5, 8, 9}
# Now try to remove 333 it is not there so will get error.
s.remove(333)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.remove(333)
KeyError: 333
#discard() --> It Removes element if it present but no error if element is not found
s
{2, 4, 5, 8, 9}
s.discard(2)
s
{4, 5, 8, 9}
s.discard(22) # We will not get any error because it is not there anyway
s
{4, 5, 8, 9}
s.pop()
4
s.pop()
5
s
{8, 9}
# clear will remove all elements
s,clear() # clear all elements
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s,clear() # clear all elements
NameError: name 'clear' is not defined
s.clear()
s
set()


## Imp fun n methods in dict##
##############################
d={101:"AI, 102:"Bigdata", 103:"cloud",104:"Devops"}
   
SyntaxError: unterminated string literal (detected at line 1)
d={101:"AI,102:"Bigdata",103:"cloud",104:"Devops"}
   
SyntaxError: unterminated string literal (detected at line 1)
d-{101:"AI,102:"Bigdata",103:"cloud",104:"Devops"}
   
SyntaxError: unterminated string literal (detected at line 1)
d={101:"AI,102:"Bigdata",103:"cloud",104:"Devops"}
   
SyntaxError: unterminated string literal (detected at line 1)
d-{101:"AI",102:"Bigdata",103:"cloud",104:"Devops"}
   
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    d-{101:"AI",102:"Bigdata",103:"cloud",104:"Devops"}
NameError: name 'd' is not defined. Did you mean: 'id'?
KeyboardInterrupt
d={101:"AI",102:"Bigdata",103:"cloud",104:"Devops"}
   
d.keys()
   
dict_keys([101, 102, 103, 104])
d.values()
   
dict_values(['AI', 'Bigdata', 'cloud', 'Devops'])
d.items() # This will display all key values
   
dict_items([(101, 'AI'), (102, 'Bigdata'), (103, 'cloud'), (104, 'Devops')])
#dict.get(key)
   
d.get(101)
   
'AI'
d.get9105)
   
SyntaxError: unmatched ')'
d.get(105)
   
d
   
{101: 'AI', 102: 'Bigdata', 103: 'cloud', 104: 'Devops'}
d.get(105)
   
# We did not get nothing because 105 is not there
   
# Now pass some value
   
d.get(105,"Python")
   
'Python'
d.get(102,"Python")
   
'Bigdata'
d
   
{101: 'AI', 102: 'Bigdata', 103: 'cloud', 104: 'Devops'}
# Here 105 will take defult value but in 2nd case we have some value so it will dispaly value from dic
   
#update()
   
d.update({106:"python",107:"ML",108:"Java"})
   
# Here we are adding 106 not in dict
   
d
   
{101: 'AI', 102: 'Bigdata', 103: 'cloud', 104: 'Devops', 106: 'python', 107: 'ML', 108: 'Java'}

d.pop()#Removes the key
   
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    d.pop()#Removes the key
TypeError: pop expected at least 1 argument, got 0
d.pop(101)
   
'AI'
d
   
{102: 'Bigdata', 103: 'cloud', 104: 'Devops', 106: 'python', 107: 'ML', 108: 'Java'}
d.pop(104)
   
'Devops'
d
   
{102: 'Bigdata', 103: 'cloud', 106: 'python', 107: 'ML', 108: 'Java'}
d.popitem()#removes the last key value pair
   
(108, 'Java')
{102: 'Bigdata', 103: 'cloud', 106: 'python', 107: 'ML'}
   
{102: 'Bigdata', 103: 'cloud', 106: 'python', 107: 'ML'}
# Clear will remove all
   
d.clear()
   
d
   
{}

#dict comprehension = Yes
   
d={i for i in range(10)}
   
d
   
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# We got a set here????
   
#{key:value,key:value.....}
   
d={i:i*i for i in range(10)}
   
d
   
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

w=["ai","ml","dl"]
   
d={i:i.upper() for i in w}
   
d
   
{'ai': 'AI', 'ml': 'ML', 'dl': 'DL'}

# Now take some and counts of each one
   
#i want count of each word by using dict comprehension
   
d={word:t.count(word) for word in t}
   
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    d={word:t.count(word) for word in t}
AttributeError: 'generator' object has no attribute 'count'
t=["ai","ml","ai","ml","dl","nlp"]
   
#i want count of each word by using dict comprehension
   
d={word:t.count(word) for word in t}
   
d
   
{'ai': 2, 'ml': 2, 'dl': 1, 'nlp': 1}
d
   
{'ai': 2, 'ml': 2, 'dl': 1, 'nlp': 1}
>>> #HEre i want swap keys and values  Home Work
...    
>>> #the output is -->{2:'ai',2:'ml'.....}
...    
>>> #by using comprehension
...    
>>> d.items()
...    
dict_items([('ai', 2), ('ml', 2), ('dl', 1), ('nlp', 1)])
>>> 
>>> for i in d.items():
...    print(i)
... 
...    
('ai', 2)
('ml', 2)
('dl', 1)
('nlp', 1)
>>> ('nlp', 1)
...    
('nlp', 1)
>>> 
>>> for k,v in d.items():
...    print(k)
...    print(v)
... 
...    
ai
2
ml
2
dl
1
nlp
1
>>> # For loop to swap
...    
>>> >>> d1={v:k for k,v in d.items()}
...    
SyntaxError: invalid syntax
>>> d1={v:k for k,v in d.items()}
...    
>>> d1
...    
{2: 'ml', 1: 'nlp'}
>>> d.items()
...    
dict_items([('ai', 2), ('ml', 2), ('dl', 1), ('nlp', 1)])
d1={k:v for k,v in d.items()}
   
dl
   
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    dl
NameError: name 'dl' is not defined. Did you mean: 'd'?
dl
   
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    dl
NameError: name 'dl' is not defined. Did you mean: 'd'?
d1
   
{'ai': 2, 'ml': 2, 'dl': 1, 'nlp': 1}
# Now reverse
   
d1={v:k for k,v in d.items()}
   
d1
   
{2: 'ml', 1: 'nlp'}
#a dict cannot have duplicate keys here so the last value overwirtes the first
   
# That is why we see only two results
   
