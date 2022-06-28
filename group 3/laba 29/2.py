import pandas as pd
import numpy as np


def create(size, x, y):
    frame = pd.Series([input("Введите значение для series: ") for i in range(size)],
                    index=[
                        [input("Введите индекс 1-го уровня: ") for i in range(size)],
                        [input("Введите индекс 2-го уровня: ") for i in range(size)]])
    print(f"series: \n{frame}")


    data_frame = pd.DataFrame(np.array([input("Введите значение для dataframe: ") for i in range(x*y)]).reshape(x, y),
                            index=[
                                [input("Введите индекс 1-го уровня: ") for i in range(x if x > y else y)],
                                [input("Введите индекс 2-го уровня: ") for i in range(x if x > y else y)]],
                            columns=[input("Введите имя колонки: ") for i in range(x if x < y else y)])
    print(f"DataFrame: \n{data_frame}")


    new_dataframe = frame.to_frame(name="")
    print(f"Конвертация series в dataframe:{new_dataframe}")


    new_series = data_frame.stack()
    print(f"Конвертация dataframe в series:\n{new_series}")


    print(f"Смена уровня осей:\n{frame.swaplevel()}")


    print(f"Сортировка индексов для конкретного уровня:\n{frame.sort_index(level=1)}")
    print(f"Сортировка данных для конкретного уровня:\n{frame.sort_values()}")

create(int(input("Введите размер: ")), int(input("Введите размер x: ")), int(input("Введите размер y: ")))
