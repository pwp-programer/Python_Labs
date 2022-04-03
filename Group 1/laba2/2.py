num1, num2 = int(input()), int(input())
counter = int(input("Введите результат умножения двух чисел: "))
if counter == num1 * num2:
	print("Правильно")
else:
	print(f"Неправильно, правильный результат {num1 * num2}")
