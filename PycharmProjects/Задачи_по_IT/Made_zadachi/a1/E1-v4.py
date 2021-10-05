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



