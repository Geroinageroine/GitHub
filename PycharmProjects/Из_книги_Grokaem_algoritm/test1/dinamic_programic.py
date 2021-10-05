word_a='hish'
word_b='vista'

if word_a[i] == word_b[j]:
    cell[i][j] = cell[i-1][j-1] +1
else cell[i][j]=0