# arr = [1, 3, 5] #=> 30
arr = [6] #=> 36
# arr = [] #=> 0

s = 0
for j in arr[::2]:
    s += j
if len(arr) == 0:
    print(s)
else:
    s *= arr[-1]
    print(s)
