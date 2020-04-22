##a = int(input('请输入一个整数：'))
##
##if a>0:
##    if a>10000:
##        print("无法表示")
##    else:
##        print("可以表示")
##    print("且大于0")
##else:
##    if a<-10000:
##        print("无法表示")
##    else:
##        print("可以表示")
##    print("且小于0")


a = int(input('请输入一个整数：'))
if a>10000:
    print("无法表示")
elif 0<a<=10000:
    print("可以表示的正数")
elif a<-10000:
    print("无法表示")
else:
    print("可以表示的负数")

