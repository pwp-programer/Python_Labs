from PIL import Image, ImageFilter

def first():
    my_image = Image.open("C:\\github\\Python_Labs\\Group 2\\laba17\\wall.jpg")
    my_image.load()

    # Поворот на 30 градусов
    img_rotate = my_image.rotate(30)
    # img_rotate.show()
    img_rotate.save("C:\\Users\\pwp\\Desktop\\img\\img_rotate.jpg")

    # Обрезка изображения
    area = (400, 400, 800, 800)
    img_crop = my_image.crop(area)
    img_crop.save("C:\\Users\\pwp\\Desktop\\img\\img_crop.jpg")
    # img_crop.show()


    # Изменить размер в 2 раза
    width, height = my_image.size
    img_change = my_image.crop((0, 0, width/2, height/2))
    # img_change.show()
    img_change.save("C:\\Users\\pwp\\Desktop\\img\\img_change.jpg")

    # Размытие
    img_blur = my_image.filter(ImageFilter.BLUR)
    # img_blur.show()
    img_blur.save("C:\\Users\\pwp\\Desktop\\img\\img_blur.jpg")


    # Создать миниатюру
    size = (128, 128)
    img = Image.open("C:\\github\\Python_Labs\\Group 2\\laba17\\wall.jpg")
    img.thumbnail(size)
    img.save("C:\\Users\\pwp\\Desktop\\img\\img_min.jpg")


    # 3 разных фильтра
    my_image = Image.open("C:\\github\\Python_Labs\\Group 2\\laba17\\wall.jpg")
    my_image.load()
    img_filter_one = my_image.filter(ImageFilter.BLUR)
    img_filter_one.save("C:\\Users\\pwp\\Desktop\\img\\img_filter_one.jpg")


    my_image = Image.open("C:\\github\\Python_Labs\\Group 2\\laba17\\wall.jpg")
    my_image.load()
    img_filter_two = my_image.filter(ImageFilter.SMOOTH)
    img_filter_two.save("C:\\Users\\pwp\\Desktop\\img\\img_filter_two.jpg")


    my_image = Image.open("C:\\github\\Python_Labs\\Group 2\\laba17\\wall.jpg")
    my_image.load()
    img_filter = my_image.filter(ImageFilter.SHARPEN)
    img_filter.save("C:\\Users\\pwp\\Desktop\\img\\img_filter.jpg")

def secondary():
    img_path = ["C:\\Users\\pwp\\Desktop\\img\\img_crop.jpg", "C:\\Users\\pwp\\Desktop\\img\\img_change.jpg","C:\\Users\\pwp\\Desktop\\img\\img_min.jpg", "C:\\Users\\pwp\\Desktop\\img\\img_filter_one.jpg"]
    
    for i in img_path:
        Img = Image.open(i)
        print("```````````````````````````````````````")
        print("Имя файла: ",Img.filename)
        print("Формат: ",Img.format)
        print("Режим: ",Img.mode)
        print("Размер: ",Img.size)
        print("Ширина: ",Img.width)
        print("Высота : ",Img.height)
        print("Цветовая палитра: ",Img.palette)
        # print("Информация об изображении: ",Img.info)
        print("```````````````````````````````````````")
