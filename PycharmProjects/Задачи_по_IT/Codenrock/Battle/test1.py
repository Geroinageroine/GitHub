a = [[[1], [0, 2]], [[2], [0, 1]], [[0, 2], [1]], [[1, 2], [0]]]
buffer=[]
print(a[0][0][0])
for i in range(len(a)):
    for j in range(len(a[i])):
        for z in range(len(a[i][j])):
            a[i][j][z]+=1

print(a)
