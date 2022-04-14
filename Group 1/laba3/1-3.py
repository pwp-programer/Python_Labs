a, b = int(input()), int(input())

counter = 0

for i in range(a-1, b, -1):
    print(i, end=" ")
    counter += 1

print(f"количество этих чисел: {counter}")
