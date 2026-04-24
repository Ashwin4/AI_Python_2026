
print("hellow ai")
try:
    a=int (input("enter a no"))
    b=int (input("enter a no"))
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("Finally Hellow")

"""
print("hellow ai")
try:
    a=int (input("enter a no"))
    b=int (input("enter a no"))
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
print("Hellow")
"""
"""
Control flow in try-except:
----------------------------
try:
    stmt1
    stmt2
    stmt3
except error:
    stmt4
stmt5


Case 1:If there is no exception  ----> 1,2,3,5--Normal termination

Case 2:if an exception raised at stmt 2 ---->1,4,5 -- Normal termination

Case 3:If an exception at stmt 2 and corresponding exception block is not matched --->1-- Abnormat termination

Case 4"If an exception at stmt1 and we came to at stmt 4? ---Abnormal termination

Conclusions:
-------------

1.Within the try block if any where exception raised then rest of the try block wont be 
executed even though handled we handled the error.So we have to only the risky code inside the
try block.

2.Not try block,Exception block can rise exception

3.If any exception which is not part of try block then that is always abnormal termination

"""
"""
print("hellow ai")
try:
    a=input("enter a no")
    b=input("enter a no")
    print(a/b)
except ZeroDivisionError as e:
    print(e)
"""
"""
Final block:
------------

is going to execute always wheather exceptoin raised or not ,wheather handled or not handled

Maintain the Clean up code seperate block that is finally
"""
"""
try:
    stmt1
    stmt2
    stmt3
except error:
    stmt4
stmt5
# Here we use finally block
try:
    stmt1
    stmt2
    stmt3
except error:
    stmt4
finally:
    stmt5

"""
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
"""
