from PIL import Image, ImageDraw, ImageFont



def first():
    # Пустой желтый фон.
    im = Image.new('RGB', (1500, 500), (219, 193, 27))
    draw = ImageDraw.Draw(im)
    # Рисуем красный эллипс с черной оконтовкой.
    draw.ellipse((100, 100, 150, 200), fill='red', outline=(0, 0, 0))
    # Рисуем "круг".
    draw.pieslice(
        xy=(425, 50, 575, 200),
        start=30, end=400, fill=(255, 255, 0),
        outline=(0, 0, 0)
    )
    # Рисуем синий прямоугольник с белой оконтовкой.
    draw.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))
    # Рисуем розовую линию с шириной в 10 пиксель.
    draw.line((350, 200, 450, 100), fill='pink', width=10)
    
    
    draw.rectangle((200, 400, 500, 300), fill='black', outline=(350, 255, 255))
    
    
    draw.polygon(
    xy=(
        (800, 300),
        (900, 200),
        (850, 400),
        (700, 400),
        (400, 200)
    ), fill='green', outline=(0, 0, 0)
    )
    
    
    # Рисуем дугу.
    draw.arc(
    xy=(155, 180, 475, 800),
    start=50, end=350,
    fill='purple'
    )
    
    # Рисуем хорду.
    draw.chord(
    xy=(625, 100, 755, 250),
    start=30, end=270,
    )
    
    
    
    draw.pieslice(
    xy=(725, 150, 855, 300),
    start=30, end=270,fill=(40, 200, 123)
    )
    
    im.save("C:\\Users\\pwp\\Desktop\\img\\1.jpg", quality=95)
    im.show()


def secondary():
    img = Image.open("C:\\Users\\pwp\\Desktop\\pic.jpg")
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype(font="C:\\Users\\pwp\Documents\\custom\\CascadiaCode\\Caskaydia Cove Nerd Font Complete Mono Windows Compatible.ttf",size=20)
    draw.text((10, 10), "Oh",font=font)
    img.show()
    
    
    draw.text((45, 10), "zrya",font=font)
    img.show()
    
    
    draw.text((10, 50), "ya",font=font)
    img.show()
    
    draw.text((45, 50), "tuda",font=font)
    img.show()
    
    draw.text((10, 95), "polez...",font=font)
    img.show()
    img.save("C:\\Users\\pwp\\Desktop\\zrya.png")


def third():
    img = Image.open("C:\\Users\\pwp\\Desktop\\pic2.jpg")
    
    watermark = Image.open("C:\\Users\\pwp\\Desktop\\zrya.png")
    
    img.paste(watermark, (25, 25))
    img.show()
