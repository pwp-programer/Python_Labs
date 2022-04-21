import math

def square(n):
    perimeter = n * 4
    square_num = n * n
    diagonally = math.sqrt(2*n)

    a = [perimeter, square_num, diagonally]

    return a

print(square(4))
