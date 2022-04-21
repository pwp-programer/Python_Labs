def bank(amount, years):
    sum = amount
    for i in range(years):
        sum += sum * 0.10
    return sum

amount, years = int(input("Введите сумму вклада: ")), int(input("Введите количество лет: "))
print(f"Сумма вклада под 10% годовых спустя {years} составляет: {bank(amount, years)}")
