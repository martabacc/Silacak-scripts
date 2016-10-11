import StringIO
import csv
from filtering import *
import array
from pprint import pprint
# yang mau ditrace :
# pub_id (1), pub_detilkodepub(2), pub_judul(15), pub_kata_kunci(16), pub_abstraksi(19), pub_halaman(22),

initiate()

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


def classify# pprint(parsedWords)
