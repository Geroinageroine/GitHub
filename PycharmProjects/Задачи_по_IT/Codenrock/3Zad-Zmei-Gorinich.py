#Можно помочь каждому бедному, но только один раз,
#и если он беднее самого богатого как минимум в 3 раза.
#Тогда его состояние удваивается (за счет богатого),
#а из ответа он исключается
#
#Вот состояния на разных шагах:
#3 14 27 58 101
#6 14 27 58 98
#6 28 27 58 84
#6 28 54 58 57
#
#Причем первым трем он помогал, а значит их вычеркнули из ответа

#kapital=[27,14,58,101,3]

kapital = list(map(int, input().split(',')))
kapital.sort()
#print(kapital)
konec=len(kapital)-1
response=''

while kapital[0]*3 <= kapital[konec]:
    kapital[konec]=kapital[konec]-kapital[0]
    kapital.pop(0)
    kapital.sort()
    konec = len(kapital)-1

i=0
for i in range(len(kapital)):
    response += str(kapital[i]) + ','
print(response[:-1])