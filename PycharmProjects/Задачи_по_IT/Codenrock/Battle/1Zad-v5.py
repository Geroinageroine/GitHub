# vvodnie dannie
spisok=[[2], ['net svyazei'], ['net svyazei']]
a=[[0], [1], [2]]



a1=[]
for i in range(len(a)):
    a1.insert(i,a[i][0])
sp=[]
no_sp=[]
stop1=False
stop2=False
i=0
k=0
k1=0
# sozdaet ot spisok n
# probuiu sozdat' troinoi spisok iz 0 1 2 3
spisok_1=[]
konec_spisok1=[]
konec_spisok2=[]
konec_spisok_real=[]
konec_spisok_real1=[]
konec_spisok_real2=[]

while k < len(a):

    i = k
    while i < len(a):
        stop1=False
        stop2=False
        for d in range(len(a)):
            no_sp.insert(d,a[d][0])

        for d in range(len(spisok)):
            spisok_1.insert(d,spisok[d][0])

        sp += a[i]

        for j in range(len(sp)):
            no_sp.remove(sp[j])

        for b in range(len(spisok_1)):
            if no_sp.count(spisok_1[b]) != 0:
                if sp.count(b) != 0:
                    stop1 = True

        if stop1 == False and len(sp) != 0 and len(no_sp)!=0:
            #print(sp,'1 day',no_sp)
            konec_spisok1.append(sp.copy())
            konec_spisok1.append(no_sp.copy())
            #print(konec_spisok1)
            konec_spisok_real1.insert(0,konec_spisok1)
            #print(konec_spisok_real)
        konec_spisok1=[]


        for b in range(len(spisok_1)):
            if sp.count(spisok_1[b]) != 0:
                if no_sp.count(b) != 0:
                    stop2 = True


        if stop2 == False and len(sp) != 0 and len(no_sp)!=0:
            #print(no_sp,'2 day', sp)
            konec_spisok2.append(no_sp.copy())
            konec_spisok2.append(sp.copy())
            #print((konec_spisok2))
            konec_spisok_real2.insert(0,konec_spisok2)

            #print(konec_spisok_real)
            k1+=1
        konec_spisok2=[]

        #print(no_sp, '3 day', sp)
        no_sp=[]
        i+=1
    sp=[]
    k+=1
konec_spisok_real=konec_spisok_real1+konec_spisok_real2
konec_spisok_real.sort()
konec_spisok_real3=[]

for i in range(len(konec_spisok_real)):
    if konec_spisok_real3.count(konec_spisok_real[i]) == 0:
        konec_spisok_real3.append(konec_spisok_real[i].copy())

konec_spisok_real3=sorted(konec_spisok_real3, key=lambda index: len(index[0]))

for i in range(len(konec_spisok_real3)):
    for j in range(len(konec_spisok_real3[i])):
        for z in range(len(konec_spisok_real3[i][j])):
            konec_spisok_real3[i][j][z]+=1

for i in range(len(konec_spisok_real3)):
    s1=str(konec_spisok_real3[i]).replace("[[","").replace("]]","").replace(" ", "").replace("],[", "  ")
    print(s1)




































































































































































































































































































































































