def mysum(a,b):
    return a+b

print('拆解元组调用：')
print(mysum(*(3,4)))
print('拆解字典调用：')
print(mysum(**{'a':3,'b':4}))
