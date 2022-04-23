def date(day, month, year):
    calendar = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

    if calendar.get(month) != None and year > 0:
        if day >= 1 and day <= calendar.get(month):
            print("Такая дата есть")
            return True
        else:
            print("Такой даты нет")
            return False
    else:
        print("Такой даты нет")
        return False

day, month, year = int(input("Введите день: ")), int(input("Введите месяц: ")), int(input("Введите год: "))
date(day, month, year)