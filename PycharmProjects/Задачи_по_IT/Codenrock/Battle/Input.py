m = int(input()) # Vsego kompanii
buffer = []
stroki=' '
i1=0
nachal_spisok=[]

while stroki!=['']:
    buffer=[]
    stroki=input().split(',')
    if stroki != ['']:
        buffer = list(map(int, stroki))

        nachal_spisok.insert(i1, buffer)
    i1+=1

kompanii=[]

for i in range(m):
    kompanii.append([0]*0)
for i in range(m):
    kompanii[i][0] = i

print(nachal_spisok)
print(kompanii)