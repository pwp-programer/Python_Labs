import turtle as t

def printer_func(size, color, f_x, f_y, s_x, s_y):
    t.penup()
    t.pensize(size)
    t.pencolor(color)
    t.goto(f_x,f_y)
    t.pendown()
    t.goto(s_x,s_y)


def mushroom():
    t.reset()
    t.speed(10)
    
    # Закрашиваем шапку гриба
    printer_func(28, "red", -27, 80, 60, 80)
    printer_func(23, "red", -25, 100, 60, 100)
    printer_func(20, "red", -20, 115, 50, 115)
    printer_func(10, "red", -20, 125, 45, 125)
    
    # Закрашиваем ножку гриба
    printer_func(35, "light yellow", 15, 13, 15, 57)
    
    # Первая нижняя точка
    printer_func(8, "white", -5, 85, 10, 85)
    printer_func(8, "white", -10, 90, 20, 90)
    printer_func(8, "white", -5, 95, 10, 95)
    
    # Вторая точка
    printer_func(15, "white", 10, 120, 30, 120)
    
    # Нижняя часть ножки гриба
    printer_func(10, "black", 0, 0, 30, 0)

    
    # Правая часть ножки гриба
    printer_func(10, "black", 35, 5, 35, 70)
    
    # Левая часть ножки гриба
    printer_func(10, "black", -5, 5, -5, 70)
    
    # Нижняя часть шапки гриба
    printer_func(10, "black", -35, 70, 65, 70)
    
    # Правая часть шапки гриба
    printer_func(10, "black", 70, 70, 70, 100)
    printer_func(10, "black", 65, 100, 65, 115)
    printer_func(10, "black", 65, 100, 65, 115)
    printer_func(10, "black", 57, 115, 57, 125)
    printer_func(10, "black", 53, 125, 40, 125)
    printer_func(10, "black", 40, 133, -5, 133)
    
    # левая часть шапки гриба
    printer_func(10, "black", -7, 125, -20, 125)
    printer_func(10, "black", -7, 125, -20, 125)
    printer_func(10, "black", -25, 125, -25, 115)
    printer_func(10, "black", -30, 115, -30, 100)
    printer_func(10, "black", -35, 100, -35, 75)

    t.mainloop()

mushroom()
