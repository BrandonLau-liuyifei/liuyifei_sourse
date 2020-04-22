for i in [1,2,3,4,5]:
    print(i)
    if i == 2:
        continue
    print(i,"的平方是：",i*i)
    if i == 4:
        break
else:
    print('循环结束！')
