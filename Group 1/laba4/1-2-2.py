import  math

s = input("Введите строку \n")

d = len(s)
f = math.ceil(float(d/2))


print(s[f-2: f+2])
