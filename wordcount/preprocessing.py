#!/usr/bin/env python
import nltk
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
symbol_list=['.',',','?','!', '@', '"', "'", '<', '>', '/', '[', ']','{','}','(',')',':',';', '…', '”', '#','$','%','^','&','*','-','+','_','=']
stop_words1=["said", "also", "like", "could", "also", "would" ,"us", "want", "via", "amp"]

filename = "D:\\MS\\2ndSem\\DIC\\Lab2\\twitterData\\trump.txt"
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

            with open('D:\MS\\2ndSem\DIC\Lab2\\twitterData\\trump_filtered.txt', 'a') as val:
                for item in wordsFiltered:
                    val.write(item+" ")
                val.write("\n" )

    # csvreader = csv.reader(f)
    # for line in csvreader:
    #     line=f.readlines()
    #     if(line):
    #         for i in range(len(line)):
    #             print(line)
    #             wordsFiltered = []
    #             words = word_tokenize(i)
    #             for w in words:
    #                 if not w in stop_words and len(w) >= 3 and not w in symbol_list and not w in stop_words1:
    #                     wordsFiltered.append(w + " ")
    #             appendFile = open('D:\MS\\2ndSem\DIC\Lab2\\twitterData\\filteredpolitic.txt', 'a')
    #             appendFile.write(wordsFiltered[i])
    #             appendFile.write("\n")
    #             appendFile.close()

# file = open("D:\MS\\2ndSem\DIC\Lab2\\twitterData\politics.txt")
# line = file.read().splitlines()
# words = line.split()
# for r in words:
#     if not r in stop_words and len(r)!=1 and not r in symbol_list and not r in stop_words1:
#         appendFile = open('D:\MS\\2ndSem\DIC\Lab2\\twitterData\\filteredpolitics.txt.txt','a')
#         appendFile.write(" "+r)
#         appendFile.close()
