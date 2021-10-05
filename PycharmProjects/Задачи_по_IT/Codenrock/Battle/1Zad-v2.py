# Sozdaem 1 den spisok
One_day=[]
Two_day=[]
#k=7
n=5 # chislo companyi
spisok=[['net svyazei'], [4], [3], [6], ['net svyazei'], ['net svyazei'], ['net svyazei']]

#if k < n-1



# snachalo perebor pi i1
# dal'she po is

result=[]
kolichestvo=0
result1=[]
k1=0

while kolichestvo<n:
    k=kolichestvo
    Two_day=[]
    One_day=[]

    for i in range(n):
        Two_day.insert(i, i)

    if spisok[k]==['net svyazei']:
        One_day.insert(k,k)
        Two_day.remove(k)
        result=[]
        d=0
        result.insert(d, One_day)
        d+=1
        result.insert(d, Two_day)
        i1=0
        result1.insert(i1,result)
    kolichestvo += 1

for i in range(2):
    One_day.insert(i,i)
One_day[i1]
for i1 in range(n):
    if One_day[i1]!=One_day[i1-1]
        One_day.insert(i2)

print(One_day)
print(result1)