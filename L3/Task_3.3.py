# list1 = [1, 2, 3, 4, 5, 6]  # => [[1, 2, 3], [4, 5, 6]]
# list1 = [1, 2, 3] # => [[1, 2], [3]]
# list1 = [1, 2, 3, 4, 5] # => [[1, 2, 3], [4, 5]]
# list1 = [1] # => [[1], []]
list1 = [] # => [[], []]
if  len(list1) == 0:
    first_list = list1
    second_list = list1[:0]
elif len(list1) % 2 != 0:
    temp = int((len(list1) + 1) / 2)
    first_list = list1[:temp]
    second_list = list1[temp:]
else:
    temp = int(len(list1) / 2)
    first_list = list1[:temp]
    second_list = list1[temp:]
my_list = []
my_list.append(first_list)
my_list.append(second_list)
print(my_list)
