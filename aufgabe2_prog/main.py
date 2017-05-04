#!/usr/bin/env python3
print('Hallo Welt!')
import nltk
from nltk.book import *
#sentence = """At eight o'clock on Thursday morning... Arthur didn't feel very good."""
#tokens = nltk.word_tokenize(sentence)
#print(tokens)
#tagged = nltk.pos_tag(tokens)
#tagged[0:6]


fileFrankenstein = open('Beispieltext_en_Frankenstein.txt', 'r')
textFrankenstein = fileFrankenstein.read().lower()
tokensFrankenstein = nltk.word_tokenize(textFrankenstein)
dist = FreqDist(tokensFrankenstein)


saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
print saying
tokens = set(saying)
print tokens
tokens = sorted(tokens)
print tokens


#fileUlysses = open('Beispieltext_en_Ulysses.txt', 'r')
#fileWarAndPeace = open('Beispieltext_en_War_and_Peace.txt', 'r')
