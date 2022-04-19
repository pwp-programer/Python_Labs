# Создание первого множества
x1 = []
for i in range(100, 201):
    x1.append(i)

# Создание второго множества
x2 = []
for i in range(100, 201):
    x2.append(i)

# Создание третьего множества
x3 = []
for i in range(100, 201):
    x3.append(i)


# Преобразование в множество
x1 = set(x1)
x2 = set(x2)
x3 = set(x3)

# print(x1, x2, x3)


# Создание мегамножества
print(x1, "\n")
y = set((x1 & x2) | (x1 | x3))
print(y)

if x1 in y:
    print("x1 in y = true")
else:
    print("x1 in y = false")

if 150 in y:
    print("150 in y = true")
else:
    print("150 in y = false")
