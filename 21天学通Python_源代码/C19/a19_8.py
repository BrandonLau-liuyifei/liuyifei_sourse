from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

a = Image.new('RGB',(200,200),'white')
drw = ImageDraw.Draw(a)
drw.rectangle((50,50,150,150),outline='red')
drw.text((60,60),'My First Draw',fill='green')
a.show()
