import StringIO
import csv

scopusData=[]


bigArray= []
parsedWords = []

keyword_JITT = ['international','journal']
keyword_SIT = ['international','seminar','conference']


def mapToArray(strings, pushToThisPlease=[]):
    strings=strings.split()
    for str in strings:
        pushToThisPlease.append(str)

def initiate():
    with open('D:/Kerja Praktek/SILACAK/scopus/scimagojr_2015.csv', 'rU') as csvf:
        testreader = csv.reader(csvf, delimiter=';', quotechar='|')
        for row in testreader:
            scopusData.append(row)

    with open('C:/Users/rona/Downloads/test_data.csv', 'r') as csvfile:
        testreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in testreader:
            bigArray.append(row)


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]