
# sozdaem spisok gde index budet raven companii a znachenie nomeru comapanii

m=6 #kolichestvo kompanii
a=[[2, 3], [1, 4], [3, 6]]

# mi sozdali vloj spisok iz napravlenii 1 cifra - eto nomer gorodaa,
# 2ya - nomer goroda s vozmojnoi dostavkoi //
# primer [[2, 4], [2, 4], [2, 4], [2, 4]] 2 gorod kontachet s 4


napravleniya = a
napravleniya.sort()
#print(napravleniya)

#[[2, 3], [2, 4], [2, 4], [4, 3]]

index=0
spisok = [] #sozdaem kuda budem zapisivat' vse napravleniya n-oi companii
l=0
nomer_company=0


while index < m:
    # napravlenii u n-ogo goroda net, to prisvaivaem emu 0 znachenie
    spisok_jelanii = [] #sozdaem spisok s indexom nomer compani iz kotorogo
                    #ishem est' li svyaz

    if napravleniya[(len(napravleniya)-1)][0] < index+1:
        napravleniya.insert(index, [index+1,'net svyazei'])

    #nachinaem s 0 i companii

    company_so_svyazyami = nomer_company
    if napravleniya[index][0] > company_so_svyazyami or napravleniya[index][0] < company_so_svyazyami:
        if napravleniya[index][0] > company_so_svyazyami:
            while napravleniya[index][0] > company_so_svyazyami: #tak kak v matrice nachalo 0

                #41 ishem kakoi pervii gorod uje imeet svyazi

                spisok_jelanii.insert(index, 'net svyazei')
                company_so_svyazyami += 1
                nomer_company +=1
        if napravleniya[index][0] < company_so_svyazyami:
            while napravleniya[index][0] < company_so_svyazyami: #tak kak v matrice nachalo 0

                #1 sozdaem drugoi spisok kotorii budet govorit est' li u n-ogo goroda
                #napravleniya
                #2 esli netu to prisvaivaem emu 0
                #3 nomer goroda budet indexom spiska
                #4 ishem kakoi pervii gorod uje imeet svyazi
                # [[2, 3], [2, 4], [2, 4], [4, 3]]
                spisok_jelanii.insert(index, 'net svyazei')
                company_so_svyazyami += 1
                nomer_company += 1
        spisok.insert(l, spisok_jelanii)
        l += 1
        spisok_jelanii = []

    if napravleniya[index][0] == company_so_svyazyami:
        # napravlenii u n-ogo goroda est', to ishem vse napravleniya1
        spisok_jelanii.insert(index, napravleniya[index][1])
        index += 1
        nomer_company += 1

        spisok.insert(l, spisok_jelanii)
    l+=1


print(spisok)
