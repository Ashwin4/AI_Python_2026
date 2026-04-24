#Exception handling - Syntex Error and Run Time error
###################
"""
we have two types of erros

syntax error
one is run time error

Exception:
----------

An unwanted or enexpected event that disturb the flow of the program is called exception.

Ex:
zerodivsion error
value error
type error
index error
key error
filenotfound error


It is highly recommended to handle the exceptions

The main objective of exception handling is graceful terimnation.

syntax:
------
try:
    risky code
except ErrorType:
    handling code


control flow in try and except:
--------------------------------
try:
    stmt1
    stmt2
    stmt3
except error:
    stmt4
stmt5


case 1: If there is no exception--->1,2,3,5--Normal termination

CAse 2: if an exception raised at stmt 2 -->1,4,5--Normal

Case 3:if an exception raised at stmt2 anc corresponding exception block is not matched-->1-->Abnormal

case 4:If an exception at stmt 4?----no stamts executed--Abnormal termination



Conclusions:
-------------

1.Within the try block if any where exception raised then rest of the try block wont be 
executed even though handled we handled the error.So we have to only the risky code inside the
try block.

2.Not try block,Exception block can rise exception

3.If any exception which is not part of try block then that is always abnormal termination

Final block:
------------

is going to execute always wheather exceptoin raised or not ,wheather handled or not handled

Maintain the Clean up code seperate block that is finally

try:
    stmt1
    stmt2
    stmt3
except error:
    stmt4
finally:
    stmt5

"""
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ValueError:
    print("value error")
    raise ZeroDivisionError("some other error raised")

except ZeroDivisionError as e:
    print(e)
    
except TypeError as t:
    print("t")

finally:
    print("hello ai")

