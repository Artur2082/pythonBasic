from typing import List


def popular_words(text: str, words: List):
    text = text.lower().split()
    result_dict = {item: text.count(item) for item in words}
    print(result_dict)
    return result_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
