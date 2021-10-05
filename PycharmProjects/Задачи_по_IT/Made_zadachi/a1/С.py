# Example 1
# N = 4 #stroki
# M = 6 #stolbec
# A=[     [0,1,1,0,1,1],
#         [1,1,1,1,1,0],
#         [1,1,1,1,0,1],
#         [0,1,0,1,1,1]
#    ]
#[['#', '.', '.', '#', '.', '.'],
# ['.', '.', '.', '.', '.', '#'],
# ['.', '.', '.', '.', '#', '.'],
# ['#', '.', '#', '.', '.', '.']]

#Example 2
#N = 8 #stroki
#M = 8 #stolbec
#A=[
#    [1,1,0,1,1,1,0,1],
#    [1,1,1,1,0,1,1,1],
#    [0,0,1,1,1,1,1,1],
#    [1,1,0,0,0,1,1,0],
#    [1,1,1,0,1,1,0,1],
#    [0,0,1,1,1,1,0,1],
#    [0,1,1,1,0,1,1,1],
#    [0,0,0,1,0,1,1,0],
#]

#[['.', '.', '#', '.', '.', '.', '#', '.'],
# ['.', '.', '.', '.', '#', '.', '.', '.'],
# ['#', '#', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '#', '#', '#', '.', '.', '#'],
# ['.', '.', '.', '#', '.', '.', '#', '.'],
# ['#', '#', '.', '.', '.', '.', '#', '.'],
# ['#', '.', '.', '.', '#', '.', '.', '.'],
# ['#', '#', '#', '.', '#', '.', '.', '#']]

N, M = map(int,input().split())
if N>=1 and N<=2000 and M>=1 and M<=2000:
    A = []
    for i in range(N):
        stroki=map(str, input())
        A.append(list(stroki))
    print(A)
    a=0

    reshetka = '#'
    tochka = '.'

    #Snachala ishem 1 v matrice
    for i in range(N):
        for j in range(M): #sozdaem elementi iz stolbci
            if A[i][j]==tochka:
                #print(i,j) # ishem A[i][j] s znacheniem ==1
                vlevo_j=j-1
                verh_i=i-1
                vpravo_j=j+1
                vniz_i=i+1
                levo, pravo, verh, vniz=0,0,0,0
    #           # Budem probovat poiti nalevo napravo vverh vniz
                #esli mojno vlevo? idem vlevo matrici

                while vlevo_j >= 0 and A[i][vlevo_j]==tochka:
                    levo += 1
                    vlevo_j -= 1
                #vpravo


                while vpravo_j < M and A[i][vpravo_j]==tochka:
                    pravo += 1
                    vpravo_j += 1

                #vverh
                while verh_i >= 0 and A[verh_i][j]==tochka:
                    verh += 1
                    verh_i -= 1

                #vniz
                while vniz_i < N and A[vniz_i][j]==tochka:
                    vniz += 1
                    vniz_i += 1
                razmer=levo+pravo+verh+vniz
                if a<razmer:
                    a=razmer
    print(a+1)
else:
    print("Не правильный ввод")









