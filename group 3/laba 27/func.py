import pandas as pd
import numpy as np

def first():
    size = int(input("Введите размер массива: "))
    arr = [int(input(f"Введите число номер {i+1}: ")) for i in range(size)]
    arr = np.array(arr)
    s = pd.Series(arr)
    print("\nСерия:")
    print(s)

def secondary():
    size = int(input("Введите размер массива: "))
    arr = [int(input(f"Введите число номер {i+1}: ")) for i in range(size)]
    ind = [int(input(f"Введите индекс номер {i+1}: ")) for i in range(size)]
    arr = np.array(arr)
    s = pd.Series(arr, ind)
    print("\nСерия:")
    print(s)
    return s

def third(s):
    print(f"Срез:\n{s[:int(input('Введите размер для среза: '))]}")

def fourth(s):
    print(s[int(input("Введите метку: "))])

def fives(s):
    n = int(input("Введите число: "))
    print([i if i > n else "" for i in s])

def sixth(s):
    print(f"Сложение серии:\n{s+s}")

def seventh():
    n, f, d = int(input("Введите размер серии: ")), int(input("Введите значение: ")), int(input("Введите индекс: "))
    s = pd.Series([f for i in range(n)], [d for i in range(n)])
    print(f"Новая серия с повторяющимися элементами:\n{s}")

def eight(s):
    u = len(pd.unique(s))
    l = len(s)
    print(f"Количество уникальных значений: {u}\
        \nКоличество повторяющихся значений: {l-u}")

def ninth(s):
    n1, n2, n3 = int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: "))
    print([i if(i == n1 or i == n2 or i == n3) else "" for i in s])

def tens():
    n = int(input("Введите размер: "))
    arr = []
    for i in range(n):
        l = int(input("Введите число: "))
        arr.append("NaN" if l == 0 else l)
    s = pd.Series(arr)
    print(s)
    return s

def eleventh(n):
    a = False
    for i in n:
        if i == "NaN":
            a = True
    if a:
        print(n)
    else:
        print("Серия не подходит условию")

def twelfth():
    d = {1: 1, 2: 2, 3: 3}
    s = pd.Series(d)
    print(f"Серия на основе списка:\n{s}")
    return s

def thirteenth():
    d = {3: 2, 2: 2, 1: 2}
    s = pd.Series(d)
    print(f"Вторая серия на основе списка:\n{s}")
    return s

def fourteenth(n1, n2):
    print(f"Умножение серий:\n{n1 * n2}\nСложение серий:\n{n1+n2}")