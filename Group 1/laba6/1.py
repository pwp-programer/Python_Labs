list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_list():
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end=" ")
        print()


print("Список до изменения: ")
print_list()


print("Список после изменения: ")
for i in range(len(list)):
    sum = 0
    for j in range(len(list[i])):
        sum += list[i][j]
        if j == len(list)-1:
            print(sum, end=" ")
        else:
            print(list[i][j], end=" ")


    print()
