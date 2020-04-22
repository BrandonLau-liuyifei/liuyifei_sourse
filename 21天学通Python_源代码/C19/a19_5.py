from PIL import Image
from PIL import ImageChops

imga = Image.open('a.jpg')
imgb = Image.open('b.jpg')

ImageChops.add(imga,imgb,1,0).show()
ImageChops.subtract(imga,imgb,1,0).show()
ImageChops.darker(imga,imgb).show()
ImageChops.lighter(imga,imgb).show()
ImageChops.multiply(imga,imgb).show()
ImageChops.screen(imga,imgb).show()
ImageChops.invert(imga).show()
ImageChops.difference(imga,imga).show()