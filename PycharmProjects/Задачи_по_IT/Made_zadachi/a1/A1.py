import time
start_time = time.time()

# my code here

print "time elapsed: {:.2f}s".format(time.time() - start_time)



#n=int(input("Введите число n: "))
#m=int(input("Введите число m: "))

#print(spisok)
n, m = map(int,input("Введите n и m").split())
spisok = list(map(int, input("Введите список, элементы разделяйте через пробел: ").split()))
#n=4
#m=10
#spisok=[6,1,2,7]
#правильный ответ 2

#для проверки
#del_spisok = spisok.pop(n-1)
#print(spisok)

#n=3
#m=5
#spisok=[3,3,3]
#правильный ответ 3

#n=10
#m=53462
#spisok=[103,35322,232,342,21099,90000,18843,9010,35221,19352]
#правильный ответ 36

count=0
i=0
sum_spisok = sum(spisok)
#print(sum_spisok)

#while sum_spisok >= m:
#    #print(sum_spisok)
#    spisok.pop(n-1)
#    #print(spisok)
#    sum_spisok = sum(spisok)
#    n-=1
#    count += 1
#print(count+1)

result=0
razmer=1
i=0

for i in range(n):
    i1=0
    while i1<n-i:
        sum_spisok = sum(spisok[i1:i1+razmer])
        if sum_spisok >= m:
            result+=1
        i1+=1
    razmer+=1
    i+=1


print(result)
