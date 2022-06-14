from PIL import Image, ImageDraw, ImageFont


def first():
    im = Image.new('RGB', (1500, 500), (219, 193, 27))
    draw = ImageDraw.Draw(im)
    draw.ellipse((100, 100, 150, 200), fill='red', outline=(0, 0, 0))
    draw.pieslice(
        xy=(425, 50, 575, 200),
        start=30, end=400, fill=(255, 255, 0),
        outline=(0, 0, 0)
    )
    # Рисуем синий прямоугольник с белой окантовкой.
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
    
    im.save(
        "C:\\github\\Python_Labs\\Group 2\\laba18\\assets\\first.png", quality=95)
    im.show()


def secondary(path_save_zrya, path_pic_one):
    img = Image.open(path_pic_one)
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype(font="C:\\Users\\pwp\Documents\\custom\\CascadiaCode\\Caskaydia Cove Nerd Font Complete Mono Windows Compatible.ttf",size=20)
    draw.text((10, 10), "Menya zvat ",font=font)
    # img.show()
    
    
    # draw.text((45, 10), "",font=font)
    # img.show()
    
    
    draw.text((10, 50), "Vldaii ya",font=font)
    # img.show()
    
    # draw.text((45, 50), "",font=font)
    # img.show()
    
    draw.text((10, 95), "cumputarshik",font=font)
    img.show()
    img.save(path_save_zrya)


def third(path_zrya, path_pic_two):
    img = Image.open(path_pic_two)
    
    watermark = Image.open(path_zrya)
    
    img.paste(watermark, (25, 25))
    img.show()
