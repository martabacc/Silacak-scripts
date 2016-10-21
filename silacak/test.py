import StringIO
import csv
from filtering import *
import sys
import datetime, time


def classify_SIT_JITT():
    for idx, data in enumerate(bigArray):
        if idx == 100: break

        id = data[0]
        detilkodepub = data[1]
        judul = data[14].lower()
        data[14] = data[14].lower()
        katakunci = data[15].lower()
        abstraksi = data[18].lower()
        issue = data[21]
        keterangan = data[23].lower()

        # already mapped data
        words = []
        mapToArray(judul, words)
        mapToArray(abstraksi, words)
        mapToArray(keterangan, words)

        classified = ''
        for idx2, word in enumerate(words):
            #         checking JITT
            for x in keyword_JITT:
                if x == word: classified = "Jurnal Internasional"

            # checking SIT
            if classified == '':
                for x in keyword_SIT:
                    if x == word: classified = "Seminar Internasional"

            if classified == '':
                if detilkodepub == 2:
                    classified = "Jurnal Nasional Tidak Terakreditasi"
                elif detilkodepub == 6:
                    classified = "Seminar Nasional/Lainnya"
                else:
                    classified = "Lainnya"

        bigArray[35] = classified


def classify_Scopus(year):

    initiate(year)

    startTime = time.time()

    scopusDatas = dataDatabase
    filename = 'result2/'+'Log_'+str(year)+'.txt'

    log = open(filename, 'w')

    log.write('---------------------------------------------------------------------------------------------------\n')
    log.write('Program dimulai ' + timeToStr(datetime.datetime.now())+'\n')
    log.write('---------------------------------------------------------------------------------------------------\n')


    for idx, data in enumerate(bigArray):


        if idx >= returnStartPoint(year) :
            # print ('processing now')
            id = data[0]
            detilkodepub = data[1]
            judul = data[14].lower()
            issue = data[21]
            # print 'Data on database : %s' % (judul)
            classified = False
            ptr = 0
            for idx2, scopusData in enumerate(scopusDatas):
                # print idx2
                # print classified
                scopusData = scopusDatas[idx2]
                titleIndex = 0
                scopusTitle = str(scopusData[titleIndex]).lower()

                if abs( len(scopusTitle) - len(judul) ) < 15:
                    maxDistance = 10
                    if len(scopusTitle) <= 15 : maxDistance = 5

                    elif levenshtein( scopusTitle , judul) <= maxDistance :
                        classified = True
                        print '[MATCH] Data %d on scopus : %s [Row %d, on row Scopus %d]' %(year, scopusTitle, idx, idx2)
                        log.write('\nData '+str(year)+' on scopus : [Row '+str(idx)+', on row Scopus '+str(idx2))
                        log.write('\nJudul Jurnal : '+judul)
                        log.write('\nJudul di Scopus : '+scopusTitle)
                        break
                else :
                    ptr += 1

            # print ('%d / %d document are excluded from filtering'%(ptr, len(scopusDatas)) )
            # if classified is False :
            #     log.write('Record '+ str(idx+1) +' bukan Jurnal Internasional Terindeks\n')


            if idx % 50 == 0 and idx!=0:
                print('Process %d comparing to %d data' %(year, idx))

    endTime = time.time()
    log.write('\n---------------------------------------------------------------------------------------------------')
    log.write('\nProgram berakhir ' + timeToStr(datetime.datetime.now()))
    log.write('\n---------------------------------------------------------------------------------------------------')

    # ending program, writing results
    log.write('\nProgram berjalan selama ' + secondsToStr(endTime-startTime))
    log.write('\nMembandingkan ' + str(len(scopusDatas))+ ' data jurnal dengan ' + str(len(bigArray)) + ' data Scopus')
    log.write('\nTerdapat '+ str(ptr) + ' jurnal yang terakreditasi internasional ' + str(year))

    log.close()
