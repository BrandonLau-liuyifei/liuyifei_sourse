from PIL import Image

imga = Image.open('a.jpg')
imgb = Image.open('b.jpg')
mask = Image.open('c.jpg')

Image.composite(imga,imgb,mask).show()