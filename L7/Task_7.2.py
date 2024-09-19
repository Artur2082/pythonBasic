def correct_sentence(text):
    text = str(text)
    if not text.endswith('.'):
        text += '.'
    if text.count('.') > 1:
        text = text.title()
    else:
        text = text.capitalize()
    print(text)
    return text




assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
