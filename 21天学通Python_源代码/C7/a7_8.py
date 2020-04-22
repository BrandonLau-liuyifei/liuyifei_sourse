def testAssert():
    for i in range(3):
        try:
            assert i<2
        except AssertionError:
            print('Raise a AssertionError!')
        print(i)
    print('end...')

testAssert()
