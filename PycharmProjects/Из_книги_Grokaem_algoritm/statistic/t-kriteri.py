import math
import scipy.stats

import numpy as np
# средние значения выборки
x1 = 45
x2 = 34

# стандартные отклонения выборки
sd1 = 9
sd2 = 10

# количество наблюдений
n1 = 100
n2 = 100

# кол-во степеней свободы
df = n1 + n2 - 2

# непосредственно расчёт t-значения
t = (x1-x2)/math.sqrt(sd1**2/n1 + sd2**2/n2)

# подсчёт p-значения
p = scipy.stats.t.sf(np.abs(t), df)*2

# вывод результата
print('t-statistic = {} p-value = {}'.format(t,p))

# подтверждение или опровержение нулевой гипотезы
if p < 0.05:
    print('H1 confirmed')
else:
    print('H1 rejected')