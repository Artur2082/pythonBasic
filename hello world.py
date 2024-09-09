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

arr = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
arr = [v for v in arr if v != 0] + [0] * arr.count(0)
print(arr)