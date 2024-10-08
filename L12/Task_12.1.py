import re
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with (codecs.open(html_file, 'r', 'utf-8') as file,
          codecs.open(result_file, 'w', 'utf-8') as file2):
        html = file.read()
        html = re.sub(r'\<[^>]*\>', '', html)
        file2.write(html)


delete_html_tags("draft.html")
