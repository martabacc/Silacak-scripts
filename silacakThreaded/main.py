from classify_function import *
from threading import *
from database import *
import threading

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, year):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.year = year
        self.db = DB()

        initiate(self.year)
        self.workQueue = []
        for idx,data in enumerate(bigArray): workQueue.append((idx,-1))

    def run(self):
        print "Starting " + self.name
        for idx, data in enumerate(bigArray) : classify_SIT_JITT()
        print "Exiting " + self.name

    def filter1(self, idx):


threadList = ["Scopus 2015","Scopus 2014","Scopus 2013","Scopus 2012","Scopus 2011","Scopus 2010","Scopus 2009"]

year = [2015,2014,2013,2012,2011,2010,2009]
queueLock = threading.Lock()
workQueue = []
threads = []
threadID = 1


if __name__ == "__main__":


    # pushing datas to array, declare comparing array
    queueLock = threading.Lock()

    for idx, tName in enumerate(threadList):
        thread = myThread(threadID, tName, year[idx])
        thread.start()
        threads.append(thread)
        threadID += 1

    # queueLock.release()

    for t in threads: t.join()

    print "Exit main thread. Thankyou :)"



