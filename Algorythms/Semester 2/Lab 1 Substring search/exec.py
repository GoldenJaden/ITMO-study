from naive import naive
from karp_hash import karp
from mur import mur
from kmp import kmp_count_substring


fib1 = fib2 = 1
n = 500
fib = '11'
a = []
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    a.append(str(fib2))
for i in range(len(a)):
    fib += a[i]
example1 = fib

cnt_dvuzn_naive = []

import time
t0 = time.perf_counter()
for i in range(10, 100):
    cnt_dvuzn_naive.append([naive(example1, str(i)), i])
t1 = time.perf_counter()
print('%.8f sec naive' % (t1-t0))

cnt_dvuzn_karp = []
t0 = time.perf_counter()
for i in range(10, 100):
    cnt_dvuzn_karp.append([karp(example1, str(i)), i])
t1 = time.perf_counter()
print('%.8f sec hash karp' % (t1-t0))

cnt_dvuzn_mur = []
t0 = time.perf_counter()
for i in range(10, 100):
    cnt_dvuzn_mur.append([mur(example1, str(i)), i])
t1 = time.perf_counter()
print('%.8f sec mur' % (t1-t0))

cnt_dvuzn_kmp = []
t0 = time.perf_counter()
for i in range(10, 100):
    cnt_dvuzn_kmp.append([kmp_count_substring(example1, str(i)), i])
t1 = time.perf_counter()
print('%.8f sec kmp' % (t1-t0))
print('Три самых часто встречающихся двузначных числа по наивному алгоритму:')
for s in sorted(cnt_dvuzn_naive, reverse=True)[:3]:
    print(f'Число {s[1]} встречалось {s[0]} раз')
print('Три самых часто встречающихся двузначных числа по алгоритму Рабина-Карпа:')
for s in sorted(cnt_dvuzn_karp, reverse=True)[:3]:
    print(f'Число {s[1]} встречалось {s[0]} раз')
print('Три самых часто встречающихся двузначных числа по алгоритму Бойера-Мура:')
for s in sorted(cnt_dvuzn_mur, reverse=True)[:3]:
    print(f'Число {s[1]} встречалось {s[0]} раз')
print('Три самых часто встречающихся двузначных числа по алгоритму Кнута-Морриса-Пратта:')
for s in sorted(cnt_dvuzn_kmp, reverse=True)[:3]:
    print(f'Число {s[1]} встречалось {s[0]} раз')



