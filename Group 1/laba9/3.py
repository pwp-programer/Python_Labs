def date(day, month, year):
    calendar = [[1, 2, 3, 4, 5], [1, 2, 3], [3, 4, 5]]

    status = False
    for i in range(len(calendar[0])):
        if day == calendar[0][i]:
            status = True
        else:
            status = False

    for j in range(len(calendar[1])):
        if month == calendar[1][j]:
            status = True
        else:
            status = False

    for q in range(len(calendar[2])):
        if year == calendar[2][q]:
            status = True
        else:
            status = False

    if status == True:
        print("Такая дата есть в календаре")
        return True
    else:
        print("Такой даты нет в календаре")
        return False

day, month, year = int(input("Введите день: ")), int(input("Введите месяц: ")), int(input("Введите год: "))
date(day, month, year)
