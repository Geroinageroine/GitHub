N = 5 # raznih cifr
M = 4  #  dlina
a=[[0], [1], [2], [3],[4],[5]]
a1=[]
for i in range(len(a)):
    a1.insert(i,a[i][0])
sp=[]
no_sp=[]

i=0
k=0
# sozdaet ot spisok n
# probuiu sozdat' troinoi spisok iz 0 1 2 3

while k < len(a):
    i = k
    while i < len(a):
        for d in range(len(a)):
            no_sp.insert(d,a[d][0])
        sp += a[i]

        for j in range(len(sp)):
            no_sp.remove(sp[j])
        print(sp,'    ',no_sp)

        no_sp=[]
        i+=1
    sp=[]
    k+=1


































































































































































































































































































































































