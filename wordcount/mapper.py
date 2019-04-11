#!/usr/bin/env python
# coding: utf-8

"""mapper.py"""

import sys
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
stop_words=set(stopwords.words("english"))
symbol_list=['.',',','?','!', '@', '"', "'", '<', '>', '/', '[', ']','{','}','(',')',':',';', '…', '”', '#','$','%','^','&','*','-','+','_','=']
stop_words1=["said", "also", "like", "could", "also", "would" ,"us", "want", "via", "amp"]
final_list=[]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.lower()
    line = line.strip()
    word_list=[]
    words = word_tokenize(line)
    for word in words:
        if word in stop_words or len(word)==1 or word in symbol_list or word in stop_words1:
            pass
        else:
            word_list.append(word)

    for word in word_list:
        final_list.append(word)
    # if (word == "test"):
    #     break;
final_list.sort()

    # increase counters
for word in final_list:
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    print ('%s\t%s' % (word, 1))
        