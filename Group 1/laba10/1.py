f = open("C:\\github\\Python_Labs\\Group 1\\laba10\\text.txt", "r", encoding="utf-8")

s = 0
fd = f.readlines()
mark_arrays = []

for i in range(10):
    a = fd[i]
    mark_arrays.append(a[-2])
    s += int(a[-2])
    if int(a[-2]) < 3:
        print(a, end="")

d = len(mark_arrays)
print(f"Средний бал по классу: {s / d}")

f.close()
