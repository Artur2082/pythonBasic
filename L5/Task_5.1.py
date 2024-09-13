from keyword import kwlist
from string import punctuation

signs_set = punctuation.replace('_', '')
signs_lst = list(signs_set)
result = True
word = input('Введіть коректну назву змінної : ')
for j in word:
    if j in signs_lst:
        result = False
for i in kwlist:
    if word == i:
        result = False
for w in word:
    if w.isupper():
        result = False
if word.startswith('__'):
    result = False
    print(result)
elif word.isdigit():
    result = False
    print(result)
elif word[0].isdigit():
    result = False
    print(result)
elif word.find(" ") != -1:
    result = False
    print(result)
else:
    print(result)
