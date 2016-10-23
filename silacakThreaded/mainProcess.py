from classify_function import *
import thread
from Queue import *
from database import *
import threading
from multiprocessing import Process

delay = 10

class P(Process):
    def __init__(self, name, year):
        super(P, self).__init__()
        initiate(self.year)
        self.name = name
        self.year = year
        self.len = 5
        self.db = DB()
        self.exitflag = False
        self.QF1 = Queue()
        self.QF2 = Queue()
        for idx in range(self.len): self.QF1.enqueue(idx)


    def run(self):
        print "Starting F1 " + self.name
        thread.start_new_thread(self.F1())
        time.sleep(delay)
        print "Starting F2 " + self.name
        thread.start_new_thread(self.F2())
        print "Exiting " + self.name

    def F1(self):
        while self.QF1.isNotEmpty() :
            now = self.QF1.front()
            result = classify_SIT_JITT(now)
            if result == 1 :
                DB.updateRow(now,1)
                print "F1 now on " + str(now)
            else :
                self.QF2.enqueue(now)
                self.QF1.dequeue()

    def F2(self):
        while self.QF1.isNotEmpty() or self.QF2.isNotEmpty():
            if self.QF2.isNotEmpty() :
                now = self.QF2.front()
                print "F2 now on " + str(now)
                DB.updateRow( now , classify_Scopus(now) )
                self.QF2.dequeue()

        exitFlag = True



PList = ["Scopus 2015","Scopus 2014","Scopus 2013","Scopus 2012","Scopus 2011","Scopus 2010","Scopus 2009"]

year = [2015,2014,2013,2012,2011,2010,2009]
workQueue = []
psx = []
threadID = 1


if __name__ == "__main__":

    for idx, tName in enumerate(Plist):
        ps = P(tName, year[idx])
        ps.start()
        psx.append(ps)

    print "Exit main thread. Thankyou :)"



