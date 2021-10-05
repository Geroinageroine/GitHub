#Prisvaevayem indexu znachenie putei iz etogo goroda

n=4 #kol-vo gorodov
m=8 #kol-vo odnostoronih napravlenii
#a= input()
#a=str(a)
#a=map(int,a.split())
#a=list(a)
a=[[2, 3], [2, 4], [2, 4], [4, 3],[2, 3], [2, 4], [2, 4], [4, 3]]
##print(a)

#napravleniya=[]

#for i in range(m):
#    #print(i)
#    napravleniya.insert(i,a)


# mi sozdali vloj spisok iz napravlenii 1 cifra - eto nomer gorodaa,
# 2ya - nomer goroda s vozmojnoi dostavkoi //
# primer [[2, 4], [2, 4], [2, 4], [2, 4]] 2 gorod kontachet s 4


napravleniya = a
napravleniya.sort()
#print(napravleniya)

#[[2, 3], [2, 4], [2, 4], [4, 3]]
index=0
spisok = [] #sozdaem kuda budem zapisivat' vse napravleniya n-ogo goroda
l=0
nomer_goroda=0

while index < m:
    # napravlenii u n-ogo goroda net, to prisvaivaem emu 0 znachenie
    spisok_napr = [] #sozdaem spisok s indexom nomer goroda iz kororogo
                    #ishem est' li dostavka

    #nachinaem s 1 go goroda

    gorod_so_svyazyami = nomer_goroda + 1
    if napravleniya[index][0] > gorod_so_svyazyami:
        while napravleniya[index][0] > gorod_so_svyazyami: #tak kak v matrice nachalo 0

            #1 sozdaem drugoi spisok kotorii budet govorit est' li u n-ogo goroda
            #napravleniya
            #2 esli netu to prisvaivaem emu 0
            #3 nomer goroda budet indexom spiska
            #4 ishem kakoi pervii gorod uje imeet svyazi
            # [[2, 3], [2, 4], [2, 4], [4, 3]]
            spisok_napr.insert(index, 0)
            gorod_so_svyazyami += 1
            nomer_goroda +=1
    if napravleniya[index][0] < gorod_so_svyazyami:
        while napravleniya[index][0] < gorod_so_svyazyami: #tak kak v matrice nachalo 0

            #1 sozdaem drugoi spisok kotorii budet govorit est' li u n-ogo goroda
            #napravleniya
            #2 esli netu to prisvaivaem emu 0
            #3 nomer goroda budet indexom spiska
            #4 ishem kakoi pervii gorod uje imeet svyazi
            # [[2, 3], [2, 4], [2, 4], [4, 3]]
            spisok_napr.insert(index, 0)
            gorod_so_svyazyami += 1
            nomer_goroda += 1
    spisok.insert(l, spisok_napr)
    l += 1
    spisok_napr = []

    if napravleniya[index][0] == gorod_so_svyazyami:
        # napravlenii u n-ogo goroda est', to ishem vse napravleniya1
        spisok_napr.insert(index, napravleniya[index][1])
        index += 1
        while index < m and napravleniya[index][0] == napravleniya[index-1][0]:
            spisok_napr.insert(index, napravleniya[index][1])
            index+=1
        nomer_goroda += 1

        spisok.insert(l, spisok_napr)
    l+=1


print(spisok)


#for i in range(2):
#    e.insert(i,a)
#
#new_spisok=[]
#new_spisok.insert(0,e)
#k=5
#j=0
#while j < k:
#    j+=1
#    new_spisok.insert(j, 0)
#new_spisok.insert(k,[7])
#new_spisok.insert(k,9)
#print(new_spisok)
