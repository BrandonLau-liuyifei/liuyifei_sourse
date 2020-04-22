def myfun():
    global a
    a = 0
    a += 3
    print('函数内a:',a)
    
a = 'external'
print('全局作用域a:',a)
myfun()
print('全局作用域a:',a)
