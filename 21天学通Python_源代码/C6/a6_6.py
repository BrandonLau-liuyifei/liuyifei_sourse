class DemoMthd:

    def __init__(self,x=0):
        self.x = x
        
    @staticmethod
    def static_mthd():
        print('调用了静态方法！')
##        print(self.x)

    @classmethod
    def class_mthd(cls):
        print('调用了类方法！')
DemoMthd.static_mthd()
DemoMthd.class_mthd()
dm = DemoMthd()
dm.static_mthd()
dm.class_mthd()
