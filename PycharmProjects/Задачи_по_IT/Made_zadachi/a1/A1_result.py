n, m = map(int,input().split())
spisok = list(map(int, input().split()))

k=0
if n>=1 and n<=50 and m>=1 and m<=10**9 and min(spisok)>=1 and max(spisok)<=10**5:
    result=0
    razmer=1
    i=0 #Количество цикла
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
else:
    print("Не правильный ввод")

