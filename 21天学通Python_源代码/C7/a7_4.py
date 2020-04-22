def testTryAll(index,i):
    stulst = ["John","Jenny","Tom"]
    try:
        print(len(stulst[index])/i)
    except:
        print("Error!")

print('Try all...Right')
testTryAll(1,2)
print('Try all...one Error')
testTryAll(1,0)
print('Try all...two Error')
testTryAll(4,0)
