from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
#pyinstaller --onefile <your_script_name>.pyprint("Метод Fsolve")
R_v = 0.0000115

R_h = 0.00001865

  #float(input("Введите R_h "))
R_s = 0.000000001 #Для поиска начального значения

def f(x):
    return (np.exp(-np.pi*R_v/x)+np.exp(-np.pi*R_h/x)-1)  # Samo uravnenie
i = 1
while i <= 30:
    root1 = optimize.fsolve(f,R_s) #fsolve is a wrapper around MINPACK’s hybrd and hybrj algorithms.
    if R_s == root1:
        R_s*=10
    i += 1  
 
print(float(root1))
#print("Значение root1 равняется ", float(root1))
#input("Нажмите ENTER, кнопку чтобы выйти")