from classify_function import *
# import thread
from Q import *
from database import *
import threading
from multiprocessing import Process

delay = 10

class P(Process):
    def __init__(self, name, year):
        super(P, self).__init__()
        self.name = name
        self.year = year
        self.threads = []

    def run(self):
        self.QF1 = Q()
        self.QF2 = Q()
        initiate(self.year)
        for idx in range(len(bigArray)): self.QF1.enqueue(idx)
gi
        if self.year == 2019 :
            t = threading.Thread(target = self.F1 )
            self.threads.append(t)
            t.start()

        time.sleep(delay)

        t = threading.Thread(target = self.F2 )
        self.threads.append(t)
        t.start()

        for t in self.threads: t.join()
        print "Exiting " + self.name

        closeConn()

    def F1(self):
        print "Starting F1 " + self.name
        while self.QF1.isNotEmpty() :
            now = self.QF1.front()
            result = classify_SIT_JITT(now)
            print "F1 now on " + str(now)
            # TODOs
            updateRow( bigArray[now][0] ,result)
            self.QF2.enqueue(now)
            self.QF1.dequeue()

    def F2(self):
        print "Starting F2 " + self.name
        while self.QF1.isNotEmpty() or self.QF2.isNotEmpty():
            if self.QF2.isNotEmpty() :
                now = self.QF2.front()
                print "F2 now on " + str(now)
                result = classify_Scopus(now)

                if result == 1:
                    # TODO
                    updateRow( bigArray[now][0] ,1)

                self.QF2.dequeue()

        exitFlag = True

# PList = ["Scopus 2015","Scopus 2014","Scopus 2013","Scopus 2012","Scopus 2011","Scopus 2010","Scopus 2009"]
# year = [2015,2014,2013,2012,2011,2010,2009]

PList = ["Scopus 2009"]
year = [2009]
workQueue = []
psx = []
threadID = 1


if __name__ == "__main__":

    for idx, tName in enumerate(PList):
        ps = P(tName, year[idx])
        ps.start()
        psx.append(ps)

    for ps in psx :
        ps.join()

    print "Exit main thread. Thankyou :)"



