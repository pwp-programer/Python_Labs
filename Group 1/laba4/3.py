s = input("Введите строку: \n")
count_big, count_small = 0, 0

for i in range(len(s)):
    if s[i].isupper():
        count_big += 1
    elif s[i].islower():
        count_small += 1

print(f"Количество символов с большой буквы:\n{count_big}\nКоличество символов с маленькой буквы:\n{count_small}")
