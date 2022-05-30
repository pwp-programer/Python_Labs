import os

def decorator_math(math_class):
    class my_class(math_class):
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def multiplication(self):
            return self.a * self.b
        def division(self):
            return 'Делить на ноль нельзя!' if self.b == 0 or self.a == 0 else self.a / self.b
    return my_class

@decorator_math
class math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b



def operation():
    while True:
        os.system("cls")
        user_operation = int(input('Введите действие: \n1-первое число a\n2-первое число b\n'))
        if user_operation == 1 or user_operation == 2:
            return user_operation

a = int(input('Введите A: '))
b = int(input('Введите B: '))
user_operation = operation()
obj = math(a, b) if user_operation == 1 else math(b, a)
os.system("cls")
print(f'Сложение: {obj.addition()}\
\nВычитание: {obj.subtraction()}\
\nУмножение: {obj.multiplication()}\
\nДеление: {obj.division()}')