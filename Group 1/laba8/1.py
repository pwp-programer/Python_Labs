school = {"1а" : 20, "1б" : 25, "1в" : 23, "2а" : 30, "2б" : 28}
print(school)


def ex2():
    number = input("Введите класс что бы узнать количество учеников в нём: ")
    if number in school:
        print(f"Количество учеников в {number}: {school[number]}")
    else:
        print("Такого класса нет")


def ex3():
    dict_1, dict_2 = {"a" : 300, "b" : 400}, {"c" : 500, "d" : 600}
    dict_1.update(dict_2)
    print(dict_1)



ex2()
ex3()
