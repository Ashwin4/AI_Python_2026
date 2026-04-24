import module1
print(module1.x)
module1.add(3,4)
module1.product(5,6)

from module import add as a
a(4,3)
# If we use * everything will print
from module import *
add(4,3)
product(8,4)
print(x)
