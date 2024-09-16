rang = input('Введіть діапазон літер через дефіс :')
start = rang[0]
end = rang[-1]
if start.islower() and end.isupper():
    letters = (''.join(chr(i) for i in range(ord(start), ord('z') + 1)) +
               ''.join(chr(i) for i in range(ord('A'), ord(end) + 1)))
    print(letters)
else:
    letters = ''.join(chr(i) for i in range(ord(start), ord(end) + 1))
    print(letters)
