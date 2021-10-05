#вот такие оптимизации могут дать + 10 тестов
#1. замена input на sys.stdin.readline()
#2. построчное считывание input очень долгое, можно использовать sys.stdin.readlines()
#3. оформлять код лучше в функцию solution(), так меньше памяти тратится.
#4. конструкции вида dict = {i: [ ] for i in range(n)} работают быстрее, чем  for i in range(n):    dict[i] = []
#
#Не проходило на 16 тесте, сейчас не проходит на 27 )

import sys

response = ''
for line in sys.stdin:  # get input strings one by one
    # do something
    n = int(line)

    lapki_jukov = 6
    lapki_paukov = 8
    jukov = 0
    paukov = 0
    i = 0
    j = 0
    list1 = []
    # ishem max kolvo paukov pri uslovii chto est' i pauki i juki
    while n >= lapki_jukov:
        line = int(line)
        n = line - i * lapki_jukov

        if n % lapki_paukov == 0:
            paukov = int(n / lapki_paukov)
            jukov = i
            stroka = str(jukov) + ',' + str(paukov)
            list1.insert(j, stroka)
            j += 1
            i += 1
        else:
            i += 1
    if paukov == 0 and jukov == 0:
        sys.stdout.write('None')

    for j in range(len(list1)):
        response += str(list1[j]) + '\n'

sys.stdout.write(response)
# print the answer to stdout

