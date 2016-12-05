
import sys, getopt
from database import *
from Init_Function import *
#def main(argv):
#    try:
#        opts, args = getopt.getopt(argv,"hi:",["ifile="])
#    except getopt.GetoptError:
#        print 'test.py -i <inputfile>'
#        sys.exit(2)
#
#    for opt, arg in opts:
#        if opt in ("-i", "--ifile"):
#        return str(arg)

if __name__ == "__main__":
    # journalTitle = main(sys.argv[1:])

    # get the data from database
    dataTable = getAllRow()
    dataIssn = getIssnRow()
    maxDistance = 2


    for keyX, x in enumerate(dataTable):
        for keyY, y in enumerate(dataIssn):
            try:
                if levenshtein(str(x['pub_keterangan']).lower , str(y['issn_judul']).lower()) <= maxDistance :
                    updateRow(x['pub_id'], JNT)
                    break
            except :
                "Error membandingkan!"
        if keyX % 100 == 0: 
            print "Membandingkan " + str(keyX) + " jurnal dengan data Issn .."
