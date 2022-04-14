list = [1, 2, 2, 3, 3, 4, 5, 6]

counter = 0

for i in range(len(list)):
    if list.count(list[i]) > counter:
        counter = list[i]
print(f"Встречается чаще всего: {counter}")
