def testTry(index,flag=False):
    stulst = ["John","Jenny","Tom"]
    if flag:
        try:
            astu = stulst[index]
        except IndexError:
            print("IndexError")
        return "Try Test Finished!"
    else:
        astu =stulst[index]
        return "No Try Test Finished!"
print("Right params testing start...")
print(testTry(1,True))
print(testTry(1))
print("Error params testing start...")
print(testTry(4,True))
print(testTry(4))
