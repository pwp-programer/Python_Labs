f = open("C:\\github\\Python_Labs\\Group 1\\laba10\\text.txt", "r", encoding="utf-8")

fd = f.readlines()
print(f"Количество строк в файле: {len(fd)}")

for i in range(len(fd)):
    print(f"Количество символов: {len(fd[i])}")

f.close()
