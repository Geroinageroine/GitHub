n = 4
dlina=1
spisok=[]
sp=''

#while dlina < n:
#    for i in range(dlina):
#
#        for j in range(n):
#            if i!=j:
#                #print('dlina= ', dlina)
#                #print(j)
#                #spisok.insert()
#    dlina+=1

N = 5 # raznih cifr
M = 4  #  dlina
a=[[0], [1], [2], [3],[4],[5]]
j=0
sp=[]
z=0
sp1=[]
sp2=[]
sp3=[]
i=0
# sozdaet ot spisok n
# probuiu sozdat' troinoi spisok iz 0 1 2 3
while i< len(a):
    sp = a[i]
    j=i+1
    print(sp)
    if j<len(a):
        sp3=sp+a[j]
        print(sp3)
        z=j+1
        if z<len(a):
            sp1=sp3+a[z]
            print(sp1)
            z1=z+1
            if z1 < len(a):
                sp2=sp1+a[z1]
                print(sp2)
                z1+=1

    i+=1



































































































































































































































































































































































