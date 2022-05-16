import math

class Sphere:
    def __init__(self, r=1, x=0, y=0, z=1):
        self.r, self.x, self.y, self.z = r, x, y, z


    def get_volume(self):
        volume = 4 / 3.0 * math.pi * self.r ** 3
        return volume

    def get_square(self):
        square = 4 * math.pi * self.r ** 2
        return square


    def get_radius(self):
        return self.r


    def get_center(self):
        return (self.x, self.y, self.z)


    def set_radius(self, r):
        self.r = r


    def set_center(self, x, y, z):
        self.x, self.y, self.z = x, y, z


    def is_point_inside(self, x, y, z):
        if x <= self.x and y <= self.y and z <= self.z:
            return True
        else:
            return False


    def __del__(self):
        print("Деструктор сработал")


use = Sphere(100, 10, 10, 10)
print(f"Объём шара ограниченной текущей сферой: {use.get_volume()}")

print(f"Площадь внешней поверхности сферы: {use.get_square()}")

print(f"Радиус сферы: {use.get_radius()}")\

print(f"Координаты центра сферы в том же порядке, в каком они задаются в конструкторе: {use.get_center()}")

print(f"Меняет радиус текущей сферы не возвращая число: {use.set_radius(4)}")

print(f"Проверка на нахождение точки внутри сферы: {use.is_point_inside(1, 1, 1)}")
