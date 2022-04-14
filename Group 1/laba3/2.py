b, a = int(input()), int(input())
print("\n")

for i in range(a, b+1):
    for j in range(0, i):
        print(i, end="")
    print()
