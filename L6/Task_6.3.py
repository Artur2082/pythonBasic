number = int(input('Введіть ціле число : '))
while number >= 9:
    result = 1
    while number != 0:
        result *= number % 10
        number = number // 10
    number = result
print(number)
