#ishem max i min cenu
n,m = 5, 3
p = (2, 3, 1, 5,5,1,5) #kortej chtobi ne izmenyat'

max_price=[]
min_price=[]

print(p)
# ishem max cenu
i=0
while i < len(p):
    if p[i] == max(p):
        max_price.insert(i, i)
        i+=1
    else:
        i+=1

#ishem min cenu
i=0
while i < len(p):
    if p[i] == min(p):
        min_price.insert(i, i)
        i+=1
    else:
        i+=1

print(max_price,min_price)
    # u min ceni doljen bit napravleniya

