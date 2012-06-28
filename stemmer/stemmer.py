# -*- coding: utf-8 -*-
import sys
from unicodedata import normalize

import Stemmer

def clean(word):
    new = ''
    for w in word:
        if not ord('a') <= ord(w[-1]) <= ord('z') and \
                not w[-1] == 'á'[-1] and \
                not w[-1] == 'é'[-1] and \
                not w[-1] == 'í'[-1] and \
                not w[-1] == 'ó'[-1] and \
                not w[-1] == 'ú'[-1] and \
                not w[-1] == 'ñ'[-1]:
            new += w

    return new

def stem(text):
    stemmer = Stemmer.Stemmer('spanish')
    output_text = ''
    stopwords = []
    sw = open('stopwords.txt', 'r')
    for line in sw:
        stopwords.append(line.strip())

    for line in text:
        l = line.split()
        l = [w.lower() for w in l]
        for word in l:
            if word not in stopwords:
                w = clean(word)
                stem = stemmer.stemWord(w)
                output_text += (stem + ' ')
