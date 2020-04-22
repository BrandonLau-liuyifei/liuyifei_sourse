x = input('输入你的总分:')
x = float(x)
if x >= 90:
    print('你的成绩为：优。')
elif x >= 80:
    print('你的成绩为：良。')
elif x >= 70:
    print('你的成绩为：中。')
elif x >= 60:
    print('你的成绩为：合格。')
else:
    print('你的成绩为：不合格。')
