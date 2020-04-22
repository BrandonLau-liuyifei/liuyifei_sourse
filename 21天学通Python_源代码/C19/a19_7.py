from PIL import Image
from PIL import ImageFilter

imga = Image.open('a.jpg')

w,h = imga.size
img_output = Image.new('RGB',(2*w,h))
img_output.paste(imga,(0,0))

fltrs = []
fltrs.append(ImageFilter.EDGE_ENHANCE)
fltrs.append(ImageFilter.FIND_EDGES)
fltrs.append(ImageFilter.GaussianBlur(4))

for fltr in fltrs:
    r = imga.filter(fltr)
    img_output.paste(r,(w,0))
    img_output.show()
