import docx
import wikipedia
import time


t0 = time.perf_counter()


special_symbols = ['.', ',', ':', '\n', '-', ')', '1', '2',
                    '3', '4', '5', '6', '7', '8', '9', '0',
                    ';', '(', ' - ', '«', '»', '—',
                    '  ', '–', '=', '==', ']', '[']


example_raw = docx.Document("corporate_values.docx")
example = ' '.join([s.text for s in example_raw.paragraphs])  # Open our docx file with text

language = "ru"
wikipedia.set_lang(language)  # import wiki page
text = wikipedia.page("Корпоративные ценности").content

for s in special_symbols:
     example = example.replace(s, ' ')  # Remove unwanted symbols from both texts
     text = text.replace(s, ' ')


example = example.split()  # Split them into separate words
text = text.split()


plagiat_len = 0

checked = []

hashes = {example[i-2] + example[i-1] + example[i]: hash(example[i-2] + example[i-1] + example[i], list(set(''.join(text) + ''.join(example)))) for i in range(2, len(example))}

for i in range(2, len(text)):
    if hash(text[i-2] + text[i-1] + text[i], list(set(''.join(text) + ''.join(example)))) in hashes.values():
        for j in range(3):
            if (i - j) not in checked:
                plagiat_len += len(text[i - j])
                checked.append(i - j)
t1 = time.perf_counter()
print('%.8f sec' % (t1-t0))

print((plagiat_len/len(example))*100, " %")
