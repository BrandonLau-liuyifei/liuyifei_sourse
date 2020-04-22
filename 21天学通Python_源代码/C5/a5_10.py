def change(aint,alst):
    aint = 0
    alst[0]=0
    alst.append(4)
    print('函数中aint:',aint)
    print('函数中alst:',alst)
    
aint = 3
alst = [1,2,3]
print('调用前aint：',aint)
print('调用前alst：',alst)
change(aint,alst)
print('调用后aint：',aint)
print('调用后alst：',alst)
