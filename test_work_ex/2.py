def func(num1, num2):
    if num1 > num2:
        return num1

    elif num2 > num1:
        return num2
    else:
        return "=="

num1, num2 = int(input()), int(input())

print(func(num1, num2))
