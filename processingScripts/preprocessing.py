#!/usr/bin/env python
import nltk
from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words=set(stopwords.words("english"))
symbol_list=['.',',','?','!', '@', '"', "'", '<', '>', '/', '[', ']','{','}','(',')',':',';', '…', '”', '#','$','%','^','&','*','-','+','_','=']
stop_words1=["said", "also", "like", "could", "also", "would" ,"us", "want", "via", "amp", "the", "year", "last","time", "first", "former",
             "this", "one", "know", "right", "time", "think", "they", "dont","omar", "need", "going", "even", "make"]

filename = "D:\\MS\\2ndSem\\DIC\\Lab2\\newsData\\newsDataOutput\\voting.txt"
#filename = "D:\\MS\\2ndSem\\DIC\\Lab2\\twitterData\\twitterDataOutput\\politics.txt"
final_list=[]
with open(filename) as f:
    for line in f:
        word_data = line.lower()
        nltk_tokens = nltk.word_tokenize(word_data)
        if(nltk_tokens.__len__()>0):
            wordsFiltered = []
            for w in nltk_tokens:
                w = lemmatizer.lemmatize(w)
                if not w in stop_words and len(w) > 3 and not w in symbol_list and not w in stop_words1:
                    wordsFiltered.append(w)

            with open('D:\MS\\2ndSem\DIC\Lab2\\newsData\\newsDataOutput\\voting_filtered.txt', 'a') as val:
            #with open('D:\MS\\2ndSem\DIC\Lab2\\twitterData\\twitterDataOutput\\politics_filtered.txt', 'a') as val:
                for item in wordsFiltered:
                    val.write(item+" ")
                val.write("\n\n")