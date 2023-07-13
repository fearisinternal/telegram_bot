from PIL import Image, ImageDraw, ImageFont, ImageColor

def add_text(filename, imagetext):
    img = Image.open(filename+".jpg")
    draw = ImageDraw.Draw(img)
    if img.width > img.height:
        fontsize = int(img.width*0.065)
    else:
        fontsize = int(img.height*0.065)

    font = ImageFont.truetype('font/Lobster 1.4 Regular.ttf', fontsize)
    x = img.width*0.5
    y = img.height*0.95
    last = len(imagetext)
    count_words = int(2*img.width/fontsize)
    point = last
    while point>0:
        point = max(0,last-count_words)
        while point<last and imagetext[point]!=' ' and point != 0:
            point+=1
        if point == last:
            point = max(0,last-count_words)
        text = imagetext[point:last]
        # thin border
        draw.text((x-1, y), text, font=font, fill='black', align='center', anchor="ms")
        draw.text((x+1, y), text, font=font, fill='black', align='center', anchor="ms")
        draw.text((x, y-1), text, font=font, fill='black', align='center', anchor="ms")
        draw.text((x, y+1), text, font=font, fill='black', align='center', anchor="ms")

        # thicker border
        draw.text((x-1, y-1), text, font=font, fill='black', align='center', anchor="ms")
        draw.text((x+1, y-1), text, font=font, fill='black', align='center', anchor="ms")
        draw.text((x-1, y+1), text, font=font, fill='black', align='center', anchor="ms")
        draw.text((x+1, y+1), text, font=font, fill='black', align='center', anchor="ms")
        draw.text((x, y), text, font=font, fill='white', align='center', anchor="ms")
        y-=fontsize
        last=point

    img.save(filename+"ans.jpg")