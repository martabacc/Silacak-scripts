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
            classified = 3
            break

    # checking SITT
    if classified == 0:
        tmp2 = []
        for x in keyword_SITT : tmp2.append(x)
        for word in words:
            # Jurnal Internasional tidak terindeks
            if str(word) in tmp2 :
                tmp2.remove(word)

            if len(tmp2) <= 1 :
                classified = 4
                break

    try:
        if classified == 0:

            if int(detilkodepub) == 2:
                # jurnal nasional tidak terakreditasi
                classified = 6
            elif int(detilkodepub) == 6:
                # seminar nasional lainnya / tidak terindeks
                classified = 7
    except :
        if classified == 0: classified = 8

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
                break

    # log.close()
    #return to the main process
    if classified :
        return 1
