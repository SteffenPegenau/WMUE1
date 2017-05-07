#!/usr/bin/env python2
import nltk
from nltk.book import *
from nltk.tokenize import RegexpTokenizer

# Tokenizer der Satzzeichen ignoriert
tokenizer = RegexpTokenizer(r'\w+')

# Nachkommastellen
decimals = 4

def probability(HN, n):
    HNinv = 1.0 / float(HN)
    nInv = 1.0 / float(n)
    prod = HNinv * nInv
    ret = prod
    print "HN=" + str(HN) + "\tn=" + str(n) + "\t=>\t" + "HNinv=" + str(HNinv) + "\tnInv=" + str(nInv) + "\tp=" + str(prod)
    return ret

# Die n (wordcount) haeufigsten Woerter fuer den text
# in Datei (fileurl) nach dem Schema
# i;Wort;Haeufigkeit\n (CSV)
# in Datei fileurl.csv speichern
def mostNWordsFor(fileurl, wordcount):
    f = open(fileurl, 'r')
    text = f.read().lower()
    f.close()
    tokens = tokenizer.tokenize(text)
    dist = FreqDist(tokens)
    words = dist.most_common(wordcount)

    N = 0
    HN = 0.0
    i = 1.0
    for w in words:
        N += w[1]
        HN += 1.0 / i
        i += 1
    print "N=" + str(N)

    sep = ";"
    stats = "i" + sep + "word" + sep + "anzahl" + sep + "rangRatio" + sep + "p" + sep + "pSumCount" + sep + "Abw\n"
    i = 1
    for w in words:
        p = probability(HN, i)
        stats += str(i) + sep
        stats += str(w[0]) + sep
        stats += str(round(w[1],0)) + sep
        stats += str(round(1/float(i),decimals)) + sep
        stats += str(round(p,decimals)) + sep
        stats += str(round(p*N,decimals)) + sep
        stats += str(round(1-float(p*N)/float(w[1]),decimals))
        stats += "\n"
        i += 1

    #save stats
    resultFile = open(fileurl + '.csv', 'w+')
    resultFile.write(stats)
    resultFile.close()

mostNWordsFor('frankenstein.txt', 40)
mostNWordsFor('samsa.txt', 40)
