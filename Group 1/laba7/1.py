# Всё первое задание разбито на функции
b = []

for i in range(1, 16):
    b.append(i)

list_number_people = tuple(b)
list_name_student = tuple(['Авсюкевич', 'Шумель', 'Аниськов', 'Баранов', 'Войтович', 'Волков',
                        'Дубровский', 'Егелявичус', 'Задора', 'Исаков', 'Казимиренко', 'Ковзель',
                        'Корнеенко', 'Костенко', 'Самойлов'])


def ex1(list_number_people, list_name_student):
    print(list_number_people)
    print(list_name_student)


def ex2(list_name_student):
    print(list_name_student[int(input("Введите число: ")) - 1])


def ex3(list_name_people):
    print(list_name_people[int(
        input("Введите число для второго списка: ")) - 1])


def ex4(list_name_student, list_number_people):
    new_list = list_name_student + list_number_people
    print(new_list)


def ex5(list_name_students, list_number_people):
    print(list_name_student[:5] + list_number_people[10:])


ex1(list_number_people, list_name_student)
ex2(list_name_student)
ex3(list_number_people)
ex4(list_name_student, list_number_people)
ex5(list_name_student, list_number_people)
