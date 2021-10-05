import numpy as np

#primer 1
#shifr = np.array([[-1,18,0],[18,-1,0],[0,0,-1]])
#kol_inf=3

#primer 2
#shifr =  np.array([[-1]])
#kol_inf=1
7
#primer 3
shifr =  np.array([[-1 ,128, 128, 128],[128, -1, 148, 160],[128, 148, -1, 128],[128, 160, 128, -1]])
kol_inf=4

print('shifr: ', shifr)


inf=np.unique(shifr)
inf = inf[inf[:] != -1]
print('Uniqalnih znachenii: ',inf)

a=len(inf)
if a>1:
    while a != kol_inf:
        inf= np.append(inf,inf[0])
        a+=1
else:
    inf=0
print('rezultat:',inf)

