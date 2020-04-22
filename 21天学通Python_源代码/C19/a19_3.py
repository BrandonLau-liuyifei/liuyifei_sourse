from PIL import Image

def div2(v):
    return v//2
imga = Image.open('a.jpg')


Image.eval(imga,div2).show()