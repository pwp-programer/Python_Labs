import pandas as pd
import numpy as np

def create_data_frame(x, y):
    data_frame = pd.DataFrame(np.array([input("Введите значение: ") for i in range(x*y)]).reshape(x, y),
                            index=[input("Введите индекс: ") for i in range(x if x > y else y)],
                            columns=[input("Введите имя колонки: ") for i in range(x if x < y else y)])

    print(f"DataFrame до изменения:\n{data_frame}\n")

    if input("Хотите удалить строку (да или нет): ") == "да":
        data_frame = data_frame.drop(index=input("Введите индекс для удаления: "), )
        print(f"DataFrame после удаления строки:\n{data_frame}\n")
    
    if input("Хотите удалить колонку (да или нет): ") == "да":
        data_frame = data_frame.drop(columns=input("Введите имя колонки для удаления: "), )
        print(f"DataFrame после удаления колонки:\n{data_frame}\n")


create_data_frame(int(input("Введите размер x: ")), int(input("Введите размер y: ")))
