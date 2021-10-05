a='((()))()()(())'
b=list(a)
#print(b)


Skobka1='('
Skobka2=')'
count_1=0
count_2=0
i1=0
kol_cicle=0

while i1 < len(b) and count_1==count_2:

    while i1 < len(b) and b[i1]==Skobka1:
        count_1+=1
        i1+=1

    while i1 < len(b) and b[i1]==Skobka2:
        count_2+=1
        i1+=1

    if count_1==count_2:
        print('Yes')
    else:
        print('No')
    count_1=0
    count_2=0
    kol_cicle+=1

print(kol_cicle)
