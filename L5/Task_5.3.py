from string import punctuation

signs_set = punctuation.replace('#', ' ')
signs_lst = list(signs_set)
text = input('Введіть текст :')
text = '#' + text.title()
for j in signs_lst:
    if j in text:
        text = text.replace(j, '')
if len(text) > 140:
    text = text[:140]
print(text)
print(len(text))
