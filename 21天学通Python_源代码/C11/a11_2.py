import fileinput
def demo_fileinput():
    with fileinput.input(['fpa.txt','fpb.txt']) as lines:
        for line in lines:
            print("总第%d行," % fileinput.lineno(),
                  "文件%s中第%d行：" %
                  (fileinput.filename(),fileinput.filelineno()))
            print(line.strip())

if __name__ == '__main__':
    demo_fileinput()
