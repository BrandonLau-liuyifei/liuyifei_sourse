def testTryFinally(index):
    stulst = ["John","Jenny","Tom"]
    af = open("my.txt",'wt+')
    try:
        af.write(stulst[index])
    except:
        pass
    finally:
        af.close()
        print("File already had been closed!")
print('No IndexError...')
testTryFinally(1)
print('IndexError...')
testTryFinally(4)
