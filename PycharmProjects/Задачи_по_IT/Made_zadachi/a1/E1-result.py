
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




#ishem cenu
n,m = 5, 3
p = (2, 3, 1, 5,5,1,5) #kortej chtobi ne izmenyat'

max_price=[]
min_price=[]

print(p)
# ishem max cenu
i=0
while i < len(p):
    if p[i] == max(p):
        max_price.insert(i, i)
        i+=1
    else:
        i+=1

#ishem min cenu
i=0
while i < len(p):
    if p[i] == min(p):
        min_price.insert(i, i)
        i+=1
    else:
        i+=1

print(max_price,min_price)
    # u min ceni doljen bit napravleniya
#max = [3, 4, 6] min = [2, 5]





# kak popast' v n-ii gorod?
# naprimer iz 4 v 1

p = (0, 1, 2, 3) #nomer goroda

sravn=[[1], [2], [3,1], [1,2]] #est' li svyazi i s kakim gorodon/ naprimer u 1 s 4 u 2 s 3,4

otkuda = 3
kuda = 0
otkuda2=0
i=0

svyazi_svyazei=[]
svyazi=[otkuda] #4
kuda_g=[kuda] #1
#(1,        2,        3,          4,      5,          6,          7) #nomer goroda
#
#[4],    [3, 4],     [0],    [3, 2],     [1]         ,[8],       [1]]
#while i<7:
    # smotrim
result=[]
stop=[]
svyazi_const=[0]
n=4 #kolichestvo gorodov
n_count=0
stop1=False
stop2=False
#vstavlyaem vse svyazi
while stop1==False and stop2==False and n_count!=n:
    razmer_svyazei=len(svyazi)
    k=0

    while k < razmer_svyazei and stop1==False:
        if sravn[svyazi[k]] != kuda:
            svyazi.insert(k, sravn[svyazi_const[k]])
            k+=1
        else:
            stop1=True
            print('nashel')

    copy_g=[]
    for i in range(k):
        copy_g.insert(i,svyazi[i])

    svyazi=copy_g

    razmer_svyazei=len(svyazi)

    # ishem u svyazei svyazi

    for i in range(len(svyazi)):
        k = 0
        while k < len(svyazi[i]) and stop2==False:
            if svyazi[i][k] != kuda:
                svyazi_svyazei.insert(k, sravn[svyazi[i][k]])
                k+=1
            else:
                stop2=True
                print('nashel')


    svyazi.insert(0, svyazi_svyazei)
    #print(otkuda_g)
    result+=svyazi
    #prevratit' svyazi v spisok (ne vloj)
    svyazi=[]
    for i in range(len(svyazi_svyazei)):
        j=0
        while j < len(svyazi_svyazei[i]):
            svyazi.insert(i,svyazi_svyazei[i][j])
            j+=1
    svyazi_const=[]

    for i in range(len(svyazi)):
        svyazi_const.insert(i,svyazi[i])
    n_count+=1
    print(svyazi)



