# kak popast' v n-ii gorod?
# naprimer iz 4 v 1

p = (1, 2, 3, 4, 5, 6, 7) #nomer goroda

sravn=[[4], [3, 4], [0], [3, 2],[1],[8],[1]] #est' li svyazi i s kakim gorodon/ naprimer u 1 s 4 u 2 s 3,4

otkuda = 4-1
kuda = 1
otkuda2=0
i=0

otkuda_g1=[]
otkuda_g=[3] #4
kuda_g=[0] #1
#(1,        2,        3,          4,      5,          6,          7) #nomer goroda
#
#[4],    [3, 4],     [0],    [3, 2],     [1]         ,[8],       [1]]
#while i<7:
    # smotrim
for k in range(len(otkuda_g)):
    otkuda_g.insert(k,sravn[otkuda_g[k]])
print(otkuda_g)
for k in range(len(otkuda_g[0])):
    otkuda_g1.insert(k, sravn[otkuda_g[0][k]])
modif=''
modif=str(otkuda_g1).replace('[',"")
modif=modif.replace(']',"")
modif=modif.replace(' ',"")
modif=modif.split(",")
modif=map(int,modif)
modif=list(modif)
print(modif)
#i+=1
otkuda_g.insert(0,modif)
print(otkuda_g)

otkuda_g=modif
print(otkuda_g)


