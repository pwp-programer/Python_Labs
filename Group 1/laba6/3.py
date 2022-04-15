list = [[1, 2, 3, 0, 5], [1, 2, 0, 4, 5], [1, 2, 3, 4, 5]]

print("Печатаем список")
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j], end=" ")
    print()


for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] == 0:
            stroka = j
            for q in range(len(list)):
                    print(list[q][stroka], end='\n')
        print()
