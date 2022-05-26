class MyClass:

    name, college, curs, people, avg_mark = "ПЗ-56", "ВГТУ", 2, 1, 0
    f = open("C:\\github\\Python_Labs\\Group 1\\laba10\\text.txt", "r", encoding="utf-8")
    fd = f.readlines()

    def __init__(self, name="", curs=0):
        self.name, self.curs = name, curs


    def __str__(self):
        print(f"Имя группы: {self.name}, Имя колледжа {self.college}, курс: {self.curs}, Количества студентов: {self.people}, Средние оценки: {self.avg_mark}")
        return ""

    def __setattr__(self, attr, val):
        if attr != "college":
            self.__dict__[attr] = val
        else:
            print("Вы не можете изменить имя колледжа")

    # Метод для обработки ситуации, когда считывается значение атрибута
    def __getattr__(self, attr):
        return "Такого поля  нет!!!!!!!!!!!!!!!!!!!!\n"

    # Метод для обработки ситуации, когда атрибут удаляется
    def __delattr__(self, attr):
    # Отображается сообщение
        print("Удалять поля запрещено!")

    def special_method(self):
        print(f"Количество студентов в файле: {len(self.fd)}")
        return len(self.fd)


obj = MyClass("Пз-52", "2")
print(obj)


obj.name = "ПЗ-56"
obj.college = "new_name"
obj.curs = 4
print(obj)
print(obj.lalalla)
del obj.name
print(obj)


obj.special_method()

mark = 0
for i in range(len(obj.fd)):
    mark += int(input("Введите оценку: "))

obj.avg_mark = mark / len(obj.fd)

print(obj)
