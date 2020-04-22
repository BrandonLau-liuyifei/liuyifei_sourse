class SmplClass:
        
    def info(self):
        print('我定义的类！')

    def mycacl(self,x,y):
        return x + y

sc = SmplClass()
print('调用info方法的结果：') 
sc.info()
print('调用mycacl方法的结果：')
print(sc.mycacl(3,4))

