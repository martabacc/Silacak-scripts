
from Init_Function import *
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
    classified = 0
    id = data[0]
    detilkodepub = data[1]
    judul = data[14].lower()
    data[14] = data[14].lower()
    katakunci = data[15].lower()
    abstraksi = data[18].lower()
    keterangan = data[23].lower()

    # already mapped data
    words = []
    mapToArray(judul, words)
    mapToArray(abstraksi, words)
    mapToArray(keterangan, words)

    tmp = []
    for x in keyword_JITT : tmp.append(x)
    for word in words:
        ptr = 0
        # Jurnal Internasional tidak terindeks
        if str(word) in tmp:
            tmp.remove(word)

        if len(tmp)  == 0:
            classified = 10
            break

    # checking SITT
    if classified == 0:
        tmp2 = []
        for x in keyword_SITT : tmp2.append(x)
        for word in words:
            # Seminar Internasional tidak terindeks
            if str(word) in tmp2 :
                tmp2.remove(word)

            if len(tmp2) <= 1 :
                classified = 11
                break

    try:
        if classified == 0:

            if int(detilkodepub) == 2:
                # jurnal nasional tidak terakreditasi
                classified = 13
            elif int(detilkodepub) == 6:
                # seminar nasional lainnya / tidak terindeks
                classified = 14
    except :
        if classified == 0: classified = 7

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

    # log = open(filename, 'a')
    data = bigArray[index]

    idx = index

    id = data[0]
    detilkodepub = data[1]
    # judul = data[14].lower()
    # yang dibandingkan ternyata keterangannya sajaaa ~

    judul = data[23].lower()
    issue = data[21]
    detilkodepub = data[1]
    # print 'Data on database : %s' % (judul)
    classified = False
    for idx2, scopusData in enumerate(scopusDatas):
        titleIndex = 0
        scopusTitle = str(scopusData[titleIndex]).lower()

        if abs( len(scopusTitle) - len(judul) ) < 15:
            maxDistance = 5
            if len(scopusTitle) <= 15 : maxDistance = 3

            elif levenshtein(scopusTitle , judul) <= maxDistance :
                print str(Pyear)+ ' '+ str(idx2) + ' ' + str(index)
                if str(scopusData[1]) == 'journal':
                    return 8
                elif str(scopusData[1]) == 'conference':
                    return 9

    return 0