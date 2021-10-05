#v zavisimosti ot max i min ceni - prisvaivaem otkuda i kuda gorod


min_price=[0,2,3] #index goroda s min cenoi
max_price=[5,4] #index goroda s max cenoi
nashel=False
dlina_min=len(min_price)
dlina_max=len(max_price)

for i in range(len(max_price)):
    index=max_price[i]
    while nashel==False and dlina_min!=len(min_price):
        dlina_min+=1



min_price_copy=[]
min_price_copy=kortej
for i in range(len(min_price)):
    min_price_copy.insert(min_price[i],"-")
minprice1=min(min_price_copy)
raznost1=maxprice-minprice1

max_price_copy=[]
max_price_copy=kortej
for i in range(len(max_price)):
    max_price_copy.insert(max_price[i],"-")
maxprice1=max(max_price_copy)
raznost2=maxprice1-minprice

if raznost2<raznost1:
    raznost=raznost1
elif raznost2==raznost1:
    raznost=0
else:
    raznost=raznost2
