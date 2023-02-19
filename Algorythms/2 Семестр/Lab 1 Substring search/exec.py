from naive import naive
from karp_hash import hash, karp
from mur import mur
import wikipedia

language = "ru"
wikipedia.set_lang(language)
example1 = wikipedia.page("Жизнь").content


template1 = 'жизнь'
import time
t0 = time.perf_counter()

naive(example1, template1)

t1 = time.perf_counter()

print('%.8f sec naive' % (t1-t0))


t0 = time.perf_counter()

karp(example1, template1)

t1 = time.perf_counter()

print('%.8f sec hash karp' % (t1-t0))


t0 = time.perf_counter()

mur(example1, template1)

t1 = time.perf_counter()

print('%.8f sec mur' % (t1-t0))

print(naive(example1, template1), 'naive result')
print(karp(example1, template1), 'karp result')
print(mur(example1, template1), 'mur result')

