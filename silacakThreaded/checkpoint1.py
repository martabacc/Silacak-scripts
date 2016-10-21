import StringIO
import csv
from filtering import *
import sys
from pprint import pprint
# yang mau ditrace :
# pub_id (1), pub_detilkodepub(2), pub_judul(15), pub_kata_kunci(16), pub_abstraksi(19), pub_halaman(22),
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
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


def classify_Scopus():
    for idx, data in enumerate(bigArray):
        if idx == 100: break

        id = data[0]
        detilkodepub = data[1]
        judul = data[14].lower()
        issue = data[21]

        classified = ''
        for idx2, scopusData in enumerate(scopusDatas):
            #         checking JITT
            titleIndex = 0
            issnIndex = 2

            if levenshtein(scopusData[0],judul) <= 10 :
                classified = 'Jurnal Internasional Terindeks Scopus'
                print '\nRecord %d recorded in scopus' %(idx)
                break

            if idx2 % 1000 == 0:
                sys.stdout.write('\rArticle ' + str(idx+1) +' compared to ' + str(idx2) + ' scopus data')

        if classified=='' :
            sys.stdout.write('\rRecord '+ str(idx+1) +' bukan Jurnal Internasional Terindeks\n')

        if idx % 50 == 0 and idx!=0:
            sys.stdout.write('\nProcessed %d data' %(idx))



initiate()

classify_Scopus()
