from PIL import Image

img = Image.open("F:/path/image.jpg")
rgba = img.convert("RGBA")
datas = rgba.getdata()
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:  # finding black colour by its RGB value
        # storing a transparent value when we find a black colour
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)  # other colours remain unchanged

rgba.putdata(newData)
rgba.save("transparent_image_2.png", "PNG")
