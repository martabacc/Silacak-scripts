import StringIO
import csv
import time
import datetime


scopus2015 = []
scopus2014 = []
scopus2013 = []
scopus2012 = []
scopus2011 = []
scopus2010 = []
scopus2009 = []


bigArray= []
parsedWords = []

keyword_JITT = ['international','journal']
keyword_SIT = ['international','seminar','conference']


def mapToArray(strings, pushToThisPlease=[]):
    strings=strings.split()
    for str in strings:
        pushToThisPlease.append(str)

def initiate():
    with open('scopus/scimagojr_2015.csv', 'rU') as csvf:
        testreader = csv.reader(csvf, delimiter=';', quotechar='|')
        for row in testreader:
            scopus2015.append(row)

    with open('scopus/scimagojr_2014.csv', 'rU') as csvf:
        testreader = csv.reader(csvf, delimiter=';', quotechar='|')
        for row in testreader:
            scopus2014.append(row)
    with open('scopus/scimagojr_2013.csv', 'rU') as csvf:
        testreader = csv.reader(csvf, delimiter=';', quotechar='|')
        for row in testreader:
            scopus2013.append(row)
    with open('scopus/scimagojr_2012.csv', 'rU') as csvf:
        testreader = csv.reader(csvf, delimiter=';', quotechar='|')
        for row in testreader:
            scopus2012.append(row)
    with open('scopus/scimagojr_2011.csv', 'rU') as csvf:
        testreader = csv.reader(csvf, delimiter=';', quotechar='|')
        for row in testreader:
            scopus2011.append(row)
    with open('scopus/scimagojr_2010.csv', 'rU') as csvf:
        testreader = csv.reader(csvf, delimiter=';', quotechar='|')
        for row in testreader:
            scopus2010.append(row)
    with open('scopus/scimagojr_2009.csv', 'rU') as csvf:
        testreader = csv.reader(csvf, delimiter=';', quotechar='|')
        for row in testreader:
            scopus2009.append(row)


    # adding database data
    with open('all_data.csv', 'r') as csvfile:
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
            insertions = previous_row[j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def secondsToStr(t):
    return "%d jam %02d menit %02d.%03d detik." % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

def timeToStr(t):
    return t.strftime("%d %B %Y %H:%M:%S")

# only for debugging

def returnStartPoint(year):
    if year==2009 : return 2550
    elif year==2010 : return 2300
    elif year==2011 :return 2150
    elif year==2012 : return 2050
    elif year==2013 : return 2000
    elif year==2014 : return 2050
    elif year == 2015 : return 2150