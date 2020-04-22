import threading
import time
class myThread(threading.Thread):
    def __init__(self,mynum):
        super().__init__()
        self.mynum = mynum

    def run(self):
        time.sleep(1)
        for i in range(self.mynum,self.mynum+5):
            print(str(i*i)+';')

def main():
    print('start...')
    ma = myThread(1)
    mb = myThread(16)
    ma.daemon = True
    mb.daemon = True
    ma.start()
    mb.start()
    print('end...')
if __name__ == "__main__":
    main()

