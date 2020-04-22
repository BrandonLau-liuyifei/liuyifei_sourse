def testTryOne(index,i):
    stulst = ["John","Jenny","Tom"]
    try:
        print(len(stulst[index])/i)
    except IndexError:
        print("Error!")

print('Try one...Right')
testTryOne(1,2)
print('Try one...one Error')
testTryOne(4,2)
print('Try one...one Error')
testTryOne(1,0)

