def delay_fun(x,y):
    def caculator():
        return x + y
    return caculator

if __name__ == '__main__':
    print('返回一个求和的函数，并不求和。')
    msum = delay_fun(3,4)
    print()
    print('调用并求和：')
    
    print(msum())
    
