import  numpy as np
from numpy import linalg
import  random

def first():
    n = int(input("Введите размер первого массива:\n"))
    
    a1, a2 = np.array([i for i in range(0, n)]), np.array([i for i in range(0, n*2)])
    
    print(f"Сумма элементов первого массива: {a1.sum()}\nСумма элементов второго массива: {a2.sum()}")
    print(f"Разность первого массива: {np.diff(a1)}\nРазность второго массива: {np.diff(a2)}")
    print(f"Произведение первого массива: {np.prod(a1)}\nПроизведение второго массива: {np.prod(a2)}")


def secondary():
    a1 = np.array([random.randint(-20, 10) for i in range(50)])
    print(f"Массив заполненный рандомными числами:\n{a1}")

    print(f"Сумма массива: {a1.sum()}")
    print(f"Минимальное число в массиве: {a1.min()}")
    print(f"Максимальное число в массиве: {a1.max()}")
    print(f"Уникальные элементы в массиве: \{np.unique(a1)}")


def third():
    n = int(input("Введите размер: "))
    a = np.ones((n, n))
    v, w = linalg.eigh(a)
    print(f"Вывод матрицы: \n{a}")
    print(f"Определить матрицы: {linalg.det(a)}")
    print(f"Собственный вектор матрицы:\n{v}")
    print(f"Собственное значение матрицы:\n{w}")


first()
secondary()
third()
