import numpy as np

n = int(input("Введите размер массива: \n"))
index, old = 0, 0;
array = np.zeros(n)
value = False
for i in range(n):
    num = int(input("Введите значение: "))
    if num <= -1:
        index = i
    array[i] = num

for i in range(index, n):
    old = array[i-1]
    if old < array[i]:
        value = True
    else:
        value = False

print(value)
