# list1 = [12, 3, 4, 10] # => [10, 12, 3, 4]
# list1 = [1] # => [1]
# list1 = [] # => []
list1 = [12, 3, 4, 10, 8]  # => [8, 12, 3, 4, 10]
if len(list1) == 0:
    print(list1)
else:
    list1.insert(0, list1.pop())
    print(list1)