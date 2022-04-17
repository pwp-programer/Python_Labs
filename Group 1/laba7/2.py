# Создание первого множества
x1 = []
for i in range(1, 21):
    x1.append(i)

# Создание второго множества
x2 = []
for i in range(10, 31):
    x2.append(i)

# Создание третьего множества
x3 = []
for i in range(1, 22, 2):
    x3.append(i)

# Преобразование в множество
x1 = set(x1)
x2 = set(x2)
x3 = set(x3)

print(x1, x2, x3)


# Создание мегамножества
y = (x1 | x2) * (x1 | x3) / (x2 + x3)
y = set(y)
print(y)
