n, k = map(int,input().split())
i1=0
spisok=[]
Str1=True

while i1<n:
    z = str(input())
    if z.isalpha():
        spisok.insert(i1, z)
    else:
        Str1=False
    i1 += 1

spisok.sort()

k1=0
if n>=1 and n<=10**5 and k>=1 and k<=n and len(min(spisok))>=1 and len(max(spisok))<=20 and Str1:
    color=0
    count=0
    while count < n:
        i=spisok.count(spisok[count])
        count+=i
        color+=1
    print(color)

else:
    print("Не правильный ввод")