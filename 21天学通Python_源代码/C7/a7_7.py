def testRaise2():
    for i in range(5):
        try:
            if i==2:
                raise NameError
        except NameError:
            print('Raise a NameError!')
        print(i)
    print('end...')

testRaise2()
