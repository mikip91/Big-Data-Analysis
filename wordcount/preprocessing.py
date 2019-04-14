#!/usr/bin/env python
import nltk
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
symbol_list=['.',',','?','!', '@', '"', "'", '<', '>', '/', '[', ']','{','}','(',')',':',';', '…', '”', '#','$','%','^','&','*','-','+','_','=']
stop_words1=["said", "also", "like", "could", "also", "would" ,"us", "want", "via", "amp"]

filename = "D:\\MS\\2ndSem\\DIC\\Lab2\\newsData\\administration.txt"
final_list=[]
with open(filename) as f:
    for line in f:
        word_data = line
        nltk_tokens = nltk.word_tokenize(word_data)
        if(nltk_tokens.__len__()>0):
            wordsFiltered = []
            for w in nltk_tokens:
                if not w in stop_words and len(w) >= 3 and not w in symbol_list and not w in stop_words1:
                    wordsFiltered.append(w)

            with open('D:\MS\\2ndSem\DIC\Lab2\\newsData\\administration_filtered.txt', 'a') as val:
                for item in wordsFiltered:
                    val.write(item+" ")
                val.write("\n\n" )