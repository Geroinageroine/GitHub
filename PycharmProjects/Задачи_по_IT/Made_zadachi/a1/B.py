#n, m = map(int,input().split())
#spisok = list(map(int, input().split()))
#n=7
#k=3
#spisok=['red','yellow','red','yellow','blue','blue','red']

#n=5
#k=5
#spisok=['orange','orange','orange','orange','orange']

#n=6
#k=4
#spisok=['red','green','green','yellow','yellow','blue']

spisok.sort()
print(spisok)


k1=0
if n>=1 and n<=10**5 and k>=1 and k<=n and len(min(spisok))>=1 and len(max(spisok))<=20 and [str(spisok[k1]).isalpha() for k1 in range(len(spisok))]:
    color=0
    count=0
    while count < n:
        i=spisok.count(spisok[count])
        count+=i
        color+=1
    print(color)

else:
    print("Не правильный ввод")