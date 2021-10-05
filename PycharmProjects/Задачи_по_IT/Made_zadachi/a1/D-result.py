#4
#((()))
#((((((
#))))))
#()()()


N = int(input())
e = []
for i in range(N):
    stroki=str(input())
    e.append(stroki)
#print(e)


# print(e)
Stop= False
# 7 while
while len(e) != 1 and Stop == False:
    # 1 - sortiruem spisok
    e.sort()
    #print(e)

    # element spiska e[0] razbivaem v novii spisok e_proverka

    e_proverka = list(e[0])



    #smotrim chto nachinaetsya s '('
    if len(e)!=0 or e_proverka[0]=='(' :

        #sumireuem 1 i 2 element spiska e
        # Zadaem uslovie chtobi konechnii element spiska ne brat'// naprimer e=[1] to e[0]=1 a e[1] - netu - oshibka
        if len(e) > 1:
            e1=(e[1])
        else:
            e1 = ''

        e_sum=e[0]+e1

        a=list(e_sum)
        #a=''.join(e_sum)

        count = 0
        while a.count('(') != len(a) and a.count(')') != len(a) and a[count] == '(':
            while a[count] == '(':
                count += 1
            if a[count] == ')':
                a.pop(count)
                a.pop(count-1)
            count = 0

    else:
        Stop = True

    #Vstavit' vmesto e[0] i e[1] peremennuyu a
    a2=''.join(a)
    if len(e) != 1:
        e.pop(0)
        e.pop(0)
    else:
        e.pop(0)
    e.insert(0,a2)

if len(e)==0 or e==['']:
    print('Yes')
else:
    print('No')
    # pravilno (((( )) ))( ) = a + d + b + c