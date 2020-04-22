class DemoInit:

    def __init__(self,x,y=0):
        self.x = x
        self.y = y

    def mycacl(self):
        return self.x + self.y

dia = DemoInit(3)
print('调用mycacl方法的结果1：')
print(dia.mycacl())

dib = DemoInit(3,7)
print('调用mycacl方法的结果2：')
print(dib.mycacl())
