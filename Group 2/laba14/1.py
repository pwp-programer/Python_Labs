class vector():
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def info(self):
        print(f"Вы создали вектор {self.name} размера {self.x, self.y}")

    def __add__(self, other):
        return f"Сложение двух векторов: {self.x + other.x, self.y + other.y}"
    def __sub__(self, other):
        return f"Вычитание двух векторов: {self.x - other.x, self.y - other.y}"

    def __mul__(self, num):
        return 

    def __eq__(self, other):
        return 

v1 = vector(input("Введите имя 1: "), int(input("Введите х: ")), int(input("Введите y: ")))
v2 = vector(input("Введите имя 2: "), int(input("Введите х: ")), int(input("Введите y: ")))

v1.info()
v2.info()

print(v1 + v2)
print(v1 - v2)
print(v1 * int(input("Введите число: ")))
print(v1 == v2)
