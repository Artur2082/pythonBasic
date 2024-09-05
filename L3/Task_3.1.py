a = int(input('Введіть число a :'))
b = int(input('Введіть число b :'))
c = input('Введіть дію +,-,* або / :')
if c == '+':
    print('a + b = ', a + b)
elif c == '-':
    print('a - b = ', a - b)
elif c == '*':
    print('a * b = ', a * b)
elif c == '/':
    if b == 0:
        print('На нуль ділити не можна ! ')
    else:
        print('a / b = ', a / b)
