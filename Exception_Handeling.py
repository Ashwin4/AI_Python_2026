Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This is from AI Session 16 Exception Handeling
for i in range(10)
SyntaxError: incomplete input
# Here we forgot : at end
10/0
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
# This is Run Time error
# type error
# value error
# file not found error

# it is highly recommended handle the error
# try and except block
#try block keep most risky code
#except block alternaitve code/handeling code

= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no10
enter a no0
Traceback (most recent call last):
  File "C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py", line 5, in <module>
    print(a/b)
TypeError: unsupported operand type(s) for /: 'str' and 'str'

= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no10
enter a no0
division by zero

= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no70
enter a no90
0.7777777777777778
Hellow

= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no4
enter a no0
division by zero
Hellow

= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no10
enter a notwenty
Traceback (most recent call last):
  File "C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py", line 5, in <module>
    b=int (input("enter a no"))
ValueError: invalid literal for int() with base 10: 'twenty'

= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no10
enter a notwenty
invalid literal for int() with base 10: 'twenty'
Hellow

= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
Traceback (most recent call last):
  File "C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py", line 63, in <module>
    stmt1
NameError: name 'stmt1' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py", line 66, in <module>
    except error:
NameError: name 'error' is not defined. Did you mean: 'OSError'?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py", line 69, in <module>
    stmt5
NameError: name 'stmt5' is not defined
>>> 
= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no30
enter a no10
3.0
Finally Hellow
>>> 
= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no10
enter a nonumber
invalid literal for int() with base 10: 'number'
Finally Hellow
>>> 
= RESTART: C:/Users/jaiam/OneDrive/2026/Training_2026/H2kInfosys-2026/Python_Codes_2026/Exception1.py
hellow ai
enter a no10
enter a no0
division by zero
Finally Hellow
