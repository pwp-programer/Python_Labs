import numpy as np
import random

def first():
    vector = np.zeros(10)
    print("Вектор размера 10 заполненный нулями: \n", vector)

def secondary():
    vector = np.array([4.6 for i in range(40)], float)
    print("Вектор размера 40 с элементами 4.6: \n", vector)
    print("Количество элементов в векторе: ", vector.size)


def third():
    a =  np.array(range(50, 1051))
    print("Вектор в пределах от 50 до 1050: \n", a)
    print("Элемент массива с индексом 100: ", a[100])
    return a

def fourth(third):
    print("Третий массив в обратном порядке: \n", third[::-1])


def fives():
    vector = np.arange(200, 399+1).reshape(20, 10)
    print("Массив размера 20 на 10 с значениями от 200 до 399 \n", vector)


def sixth():
    a = np.ones((30, 30))
    print("Матрица размера 30 на 30, состоящая из единиц: \n", a)


def seventeen():
    a = np.array([random.randint(0, 5) for i in range(25)]).reshape((5, 5))
    print("Матрица 5х5х5: \n", a)


def eighth(i, size):
    i+=1
    if i == 1 or i == size:
        print(np.array([1 for i in range(size-1)]))
    else: 
        print(np.array([1 if i == 0 or i == size-2 else 0 for i in range(size-1)]))
    if (i < size):
        eighth(i, size)


def nine(size):
    a = np.array([0 if i % 2 == 0 else 1 for i in range(size*size)])
    print(a.reshape(size, size))
