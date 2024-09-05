# list = [12, 3, 4, 10] # => [10, 12, 3, 4]
# list = [1] # => [1]
# list = [] # => []
list = [12, 3, 4, 10, 8]  # => [8, 12, 3, 4, 10]
if len(list) == 0:
    print(list)
else:
    list.insert(0, list.pop())
    print(list)
