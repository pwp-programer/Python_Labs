list = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [2, 2, 2, 2, 2]]

def print_list(n):
    for i in range(len(list)):
        print(list[n][i], end=" ")
    print()

print_list(0)
print_list(len(list) - 1)
