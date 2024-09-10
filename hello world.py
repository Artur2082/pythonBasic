import math
from array import array


print('Hello World')

a = array('i',[0,1,2,3])
a.reverse()
a.insert(0,45)
print(a)

def sum (a,b):
    a = math.pow(a,2)
    return a+b
print(sum(9,300))

for greetings in range(len(a)):
    print('Hello World')



