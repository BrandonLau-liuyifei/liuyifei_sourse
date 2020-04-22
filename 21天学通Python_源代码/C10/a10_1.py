from foo import foo_fun

name = 'Current module'
def bar():
    print('当前模块中函数bar:')
    print('变量name：',name)

def call_foo_fun(fun):
    fun()

if __name__ == '__main__':
    bar()
    print()
    foo_fun()
    print()
    call_foo_fun(foo_fun)

