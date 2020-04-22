from PIL import Image

imga = Image.open('a.jpg')
imgb = Image.open('b.jpg')

Image.blend(imga,imgb,0.5).show()