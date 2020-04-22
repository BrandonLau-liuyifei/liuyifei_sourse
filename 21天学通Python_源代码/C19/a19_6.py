from PIL import Image
from PIL import ImageEnhance

imga = Image.open('a.jpg')

w,h = imga.size
img_output = Image.new('RGB',(2*w,h))
img_output.paste(imga,(0,0))


nhc = ImageEnhance.Color(imga)
nhb = ImageEnhance.Brightness(imga)
for nh in [nhc,nhb]:
    for ratio in [0.6,1.8]:
        b = nh.enhance(ratio)
        img_output.paste(b,(w,0))
        img_output.show()
# ImageEnhance.Contrast(imga).show()
# ImageEnhance.Brightness(imga).show()
# ImageEnhance.Sharpness(imga).show()