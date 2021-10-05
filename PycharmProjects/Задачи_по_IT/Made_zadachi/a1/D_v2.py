a = ')(((())())()'
b = '))('
d = '))'
c = ')'
j = '(()'

e = [a, b, c, d, j]
# print(e)

e.sort()
print(e)

a = list(a)

for i in range(e):
    a[i]

count = 0
while a.count('(') != len(a) and a.count(')') != len(a) and a[count] == '(':
    while a[count] == '(':
        count += 1
    if a[count] == ')':
        a.pop(count - 1)
        a.pop(count)
    count = 0
# print(a)

# pravilno (((( )) ))( ) = a + d + b + c
