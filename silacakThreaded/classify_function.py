import StringIO
import csv
from Init_Function import *
import sys
import datetime, time

'''
5. Jurnal Nasional Terakreditasi

'''


def classify_SIT_JITT(index):

    '''
    Mengklasifikasikan berdasarkan kata saja
    Mereturn dengan nilai berikut

    3. Jurnal Internasional tidak terindeks
    4. Seminar Internasional tidak terindeks
    6. Jurnal Nasional Tidak Terakreditasi
    7. Seminar Nasional
    8. Lain-lain

    :param index of array:
    :return the value of filtered things
    '''

    data = bigArray[index]
    classified = 8
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

    tmp = keyword_JITT
    for idx2, word in enumerate(words):
        ptr=0
        # Jurnal Internasional tidak terindeks
        for x in tmp:
            if x == word:
                ptr+=1
                tmp.remove(x)
        if ptr >= 2 : classified = 3

    # checking SITT
    if classified == 8:
        tmp = keyword_SITT
        ptr=0
        for x in tmp:
            if x == word:
                ptr+=1
                tmp.remove(x)
        if ptr >= 2 : classified = 4

    if classified == 8:
        if detilkodepub == 2:
            # jurnal nasional tidak terakreditasi
            classified = 6
        elif detilkodepub == 6:
            # seminar nasional lainnya / tidak terindeks
            classified = 7

#     return value to the main process
    return classified


def classify_Scopus(index):
    '''
    klasifikasi berdasarkan
    1.Jurnal Internasional Terindeks
    2.Seminar Internasional Terindeks
    '''
    startTime = time.time()

    scopusDatas = scopusArray
    # filename = 'result2/'+'Log_'+str(year)+'.txt'

    # log = open(filename, 'a')
    data = bigArray[index]

    idx = index

    id = data[0]
    detilkodepub = data[1]
    judul = data[14].lower()
    issue = data[21]
    # print 'Data on database : %s' % (judul)
    classified = False
    for idx2, scopusData in enumerate(scopusDatas):
        scopusData = scopusDatas[idx2]
        titleIndex = 0
        scopusTitle = str(scopusData[titleIndex]).lower()

        if abs( len(scopusTitle) - len(judul) ) < 15:
            maxDistance = 10
            if len(scopusTitle) <= 15 : maxDistance = 5

            elif levenshtein(scopusTitle , judul) <= maxDistance :
                classified = True
                # print '[MATCH] Data %d on scopus : %s [Row %d, on row Scopus %d]' %(year, scopusTitle, idx, idx2)
                # log.write('\nData '+str(year)+' on scopus : [Row '+str(idx)+', on row Scopus '+str(idx2))
                # log.write('\nJudul Jurnal : '+judul)
                # log.write('\nJudul di Scopus : '+scopusTitle)
                break

    log.close()
    #return to the main process
    if classified :
        return 1
    else:
        return 0
