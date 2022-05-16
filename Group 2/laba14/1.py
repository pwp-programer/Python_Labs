class vector():
    def __init__(self, number):
        self.number = number


    def __add__(self, x):
        v = self.number + x
        tmp = vector(v)
        print(tmp)

a = vector(10)
b = a + 5
print(a)
print(b)
