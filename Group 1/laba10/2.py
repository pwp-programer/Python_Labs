file_name = input("Введите название для файла: ")

f = open(file_name+".txt", "w+")

print("Введите текст который вы хотите записать в файл: ")


while True:
    first_input = input()
    if first_input == "":
        break
        f.close()
    else:
        f.write(first_input + "\n")
