#print('Zadanie 2')
a=[12,13,7,29,32,3,3,3,1,1]
delitel=4

a = list(map(int, input().split(',')))
delitel = int(input())

response=''

a.sort(reverse=True)
kolichestvo=0
list1=[]
j=0
konec = len(a) - 1

while len(a) != 1 and a[konec]!=0:

    if len(a) > 2 and konec!=1:

        while len(a) > 2 and a[0]//a[konec] < delitel:
            #32 29 13 12 7 3 3
            a.pop(0)
            if konec!=len(a)-1:
                konec=len(a)-1


        while a[0]//a[konec] >= delitel:

            while a[0]//a[konec] > delitel:
                konec-=1

            while a[0]//a[konec] == delitel:
                kolichestvo += 1
                list1.insert(j, str(a[konec]) +',' + str(a[0]))
                j+=1
                konec-=1
                ##print(kolichestvo)
        a.pop(0)
        konec = len(a) - 1


    else:
        if a[0] // a[1] == delitel:
            kolichestvo += 1
            list1.insert(j, str(a[konec]) +',' + str(a[0]))
            a.pop(0)
        else:
            a.pop(0)
list1.sort()
i=0
for i in range(len(list1)):
    response += str(list1[i]) + '\n'
print(response)













