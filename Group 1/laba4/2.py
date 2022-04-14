s = input("Введите строку: \n")
d = 0

for i in range(len(s)):
    if s[i].isdigit():
        d += int(s[i])

print(d)
