def is_even(number):
    even = True
    number = str(number)
    if number[-1] in '13579':
        even = False
    return even


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('Ok')
