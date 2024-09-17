import string

rang = input('Введіть діапазон літер через дефіс :')
start = string.ascii_letters.index(rang[0])
end = string.ascii_letters.index(rang[-1])
letters = string.ascii_letters[start:end +1]
print(letters)