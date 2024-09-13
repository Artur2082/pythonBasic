from random import randint

my_list = [randint(1, 10) for i in range(randint(3, 10))]
print(my_list)
new_list = [my_list[0], my_list[2], my_list[-2]]
print(new_list)
