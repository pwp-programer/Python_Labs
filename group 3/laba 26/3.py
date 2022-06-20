import  numpy as np


n = int(input("Введите размер массива: "))
a = np.array([i for i in range(n, 0 , -1)])
print(f"Массив до изменения: \n{a}")
print(f"Массив после изменения: \n{np.sort(a)}")
