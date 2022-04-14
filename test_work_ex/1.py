mark_list = []
plus_mark, minus_mark = 0, 0
for i in range(5):
    try:
        a = int(input(f"Введите оценку под номером {i}: "))
        if a >= 1 and a <= 10:
            mark_list.append(a)
    except ValueError:
        print("Ошибка, введите цифру от 1 до 10")

for i in mark_list:
    if i >= 5:
        plus_mark += 1
    else:
        minus_mark += 1

print(f"Положительное количество оценок: {plus_mark}")
print(f"Отрицательное количество оценок: {minus_mark}")
