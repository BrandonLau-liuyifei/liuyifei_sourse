def cube(name,**nature):
    all_nature = {'x':1,
                  'y':1,
                  'z':1,
                  'color':'white',
                  'weight':1}
    all_nature.update(nature)
    print(name,"立方体的属性:")
    print('体积:',all_nature['x']*all_nature['y']*all_nature['z'])
    print('颜色:',all_nature['color'])
    print('重量:',all_nature['weight'])

cube('first')
cube('second',y=3,color='red')
cube('third',z=2,color='green',weight=10)
