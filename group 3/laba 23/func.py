import numpy as np

def first():
    a = np.array([1, 2, 3, 4, 5], float)
    print(a)
    print(type(a))


def secondary():
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], int)
    print(a[:int(input("Введите число для крайней границы первого среза: "))])
    print(a[:int(input("Введите число для крайней границы второго среза: "))])
    return a

def third():
    a = np.array(range(12), int)
    print("Массив до изменений: ", a)
    print("Массив после изменений: ", a.reshape(3, 4))
    print("Количество элементов в массиве: ", a.size)
    return a


def fourth():
    a = np.array(range(15), int)
    print("Число номер 1 входит в массив " if int(input("Введите число номер 1: ")) in a else "Числа номер 1 нет в массиве")
    print("Число номер 2 входит в массив " if int(input("Введите число номер 2: ")) in a else "Числа номер 2 нет в массиве")


def fifth():
    a = np.array(range(1, 31, 1), int)
    print("Массив на 30 чисел с размером 1 на 30: ", a)
    a = a.reshape(3, 10)
    print("Массив на 30 чисел с размером 3 на 10: ", a)


def sixth(sec, three):
    # print("Объединение второго массива: ", sec.flatten())
    print("Объединение третьего массива: ", three.flatten())
    fourth = np.concatenate([sec, three])
    print("Объединение второго и третьего массива в четвёртый: ", fourth)


def seventh():
    a = np.array(range(1, 101, 4))
    print("Массив от 1 до 101 с шагом 4: ", a)


def eight():
    a = np.ones((10, 10))
    print("Массив заполненый 1 с размером 10 на 10: \n", a)
    a = np.zeros((10, 10))
    print("Массив заполненный нулями с размером 10 на 10: \n", a)


def nine():
    a = np.array(range(1, 200, 2)) # 200 - что бы получить по итогу 100 значений
    print("Массив на 100 элементов с шагом 2: \n", a)
    print(a.size)
    a.reshape(25, 4)
    print("Массив на 100 элементов с размером 25 на 4: \n", a)


def ten():
    a = np.zeros((15, 15))
    print("Нулевая матрица: \n", a)
    a = np.eye(15, k=7)
    print("Массив с диагональю на 8-ках: \n", a)
