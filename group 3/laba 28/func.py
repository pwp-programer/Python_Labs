import pandas as pd
import numpy as np


def first():
    amount, d = int(input("Количество колонок:\n")), {}
    for i in range(amount):
        t = {input("Введите имя для колонки: "): [input("Введите значение: ") for i in range(amount)]}
        d = d | t
    frame = pd.DataFrame(d)
    print(frame)
    return d


def second(d):
    index = [input("Введите индекс: ") for i in range(len(d))]
    frame = pd.DataFrame(d, index=index)
    print(frame)


def third(d):
    frame = pd.DataFrame(d)
    print(f"Имя колонок:\n{frame.columns}")
    print(f"Весь набор данных:\n{frame.values}")


def fourth(d):
    frame = pd.DataFrame(d)
    print(f"Первая строка:\n{frame.values[0]}")
    print(f"Первые три строки:\n{frame.values[:3]}")


def five(d):
    frame = pd.DataFrame(d)
    print(f"Часть DataFrame: \n{frame.head(int(input('Размер: ')))}")


def sixth(d):
    n = {input("Введите имя столбца: "): [input("Введите значение: ") for i in range(len(d))]}
    d = d | n
    frame = pd.DataFrame(d)
    print(frame)


def seventh(d):
    frame, find_value = pd.DataFrame(d), input("Введите значение для поиска:\n")
    print(frame.isin([find_value, find_value]))

def eighth(d):
    frame = pd.DataFrame(d)
    print(frame.columns)
    de = input("Введите имя колонки для удаления: ")
    if de in frame.columns:
        del frame[de]
        print(frame)
    else:
        print("Такой колонки нет")
        eighth(d)

def ninth(d):
    frame = pd.DataFrame(d)
    print(f"До транспонирования:\n{frame}")
    print(f"После транспонирование:\n{frame.T}")
