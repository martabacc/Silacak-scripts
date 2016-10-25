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
        self.QF3 = Q()
        self.QF4 = Q()
        initiate(self.year)


        x = len(scopusArray)
        print x
        print x/2
        print x/4
        print int(x/2)
        time.sleep(5)
        for idx in range( int(x/4) ): self.QF1.enqueue(idx)
        for idx in range( int(x/2) , int(x/2) ): self.QF2.enqueue(idx)
        for idx in range( int(x/2), int(0.75 * x)): self.QF3.enqueue(idx)
        for idx in range( int(0.75 * x) , x): self.QF4.enqueue(idx)

        t = threading.Thread(target = self.F1 )
        self.threads.append(t)
        t = threading.Thread(target = self.F2 )
        self.threads.append(t)
        t = threading.Thread(target = self.F3 )
        self.threads.append(t)
        t = threading.Thread(target = self.F4 )
        self.threads.append(t)

        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()
        print "Exiting " + self.name

        closeConn()

    # def F1(self):
    #     print "Starting F1 " + self.name
    #     while self.QF1.isNotEmpty() :
    #         now = self.QF1.front()
    #         result = classify_SIT_JITT(now)
    #         print "F1 now on " + str(now)
    #         # TODOs
    #         updateRow( bigArray[now][0] ,result)
    #         self.QF2.enqueue(now)
    #         self.QF1.dequeue()

    def F1(self):
        print "Starting F1 " + self.name
        while self.QF1.isNotEmpty():
            if self.QF1.isNotEmpty() :
                now = self.QF1.front()
                print "F1 now on " + str(now)
                result = classify_Scopus(now)
                if result == 1:
                    # TODO
                    updateRow( bigArray[now][0] ,1)

                self.QF1.dequeue()


    def F2(self):
        print "Starting F2 " + self.name
        while self.QF2.isNotEmpty():
            if self.QF2.isNotEmpty() :
                now = self.QF2.front()
                print "F2 now on " + str(now)
                result = classify_Scopus(now)

                if result == 1:
                    updateRow( bigArray[now][0] ,1)

                self.QF2.dequeue()

    def F3(self):
        print "Starting F3 " + self.name
        while self.QF3.isNotEmpty():
            if self.QF3.isNotEmpty():
                now = self.QF3.front()
                print "F3 now on " + str(now)
                result = classify_Scopus(now)

                if result == 1:
                    # TODO
                    updateRow(bigArray[now][0], 1)

                self.QF3.dequeue()

    def F4(self):
        print "Starting F4 " + self.name
        while self.QF4.isNotEmpty():
            if self.QF4.isNotEmpty():
                now = self.QF4.front()
                print "F4 now on " + str(now)
                try :
                    result = classify_Scopus(now)

                    if result == 1:
                        # TODO
                        updateRow(bigArray[now][0], 1)

                    self.QF4.dequeue()
                except : continue


PList = ["Scopus 2015","Scopus 2014","Scopus 2013","Scopus 2012","Scopus 2011","Scopus 2010","Scopus 2009"]
year = [2015,2014,2013,2012,2011,2010,2009]

# PList = ["Scopus 2009"]
# year = [2009]
workQueue = []
psx = []
threadID = 1


if __name__ == "__main__":

    for idx, tName in enumerate(PList):
        ps = P(tName, year[idx])
        psx.append(ps)

    for ps in psx :
        ps.start()
        ps.join()

    print "Exit main thread. Thankyou :)"



