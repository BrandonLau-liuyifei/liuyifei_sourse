class PrntA:

    namea = 'PrntA'
    def set_value(self,a):
        self.a = a

    def set_namea(self,namea):
        PrntA.namea = namea

    def info(self):
        print('PrntA:%s,%s' % (PrntA.namea,self.a))

class PrntB:

    nameb = 'PrntB'

    def set_nameb(self,nameb):
        PrntB.nameb = nameb

    def info(self):
        print('PrntB:%s' % (PrntB.nameb,))

class Sub(PrntA,PrntB):
    pass

class Sub2(PrntB,PrntA):
    pass

class Sub3(PrntA,PrntB):

    def info(self):
        PrntA.info(self)
        PrntB.info(self)
        
print('使用第一个子类：')
sub = Sub()
sub.set_value('aaaa')

sub.info()
sub.set_nameb('BBBB')

sub.info()
print('使用第二个子类：')
sub2= Sub2()
sub2.set_value('aaaa')

sub2.info()
sub2.set_nameb('BBBB')

sub2.info()
print('使用第三个子类：')
sub3= Sub3()
sub3.set_value('aaaa')

sub3.info()
sub3.set_nameb('BBBB')

sub3.info()
