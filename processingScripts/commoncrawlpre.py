#!/usr/bin/env python
import nltk
from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

#ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words=set(stopwords.words("english"))
symbol_list=['.',',','?','!', '@', '"', "'", '<', '>', '/', '[', ']','{','}','(',')',':',';', '…', '”', '#','$','%','^','&','*','-','+','_','=']
stop_words1=["said", "also", "like", "could", "also", "would" ,"us", "want", "via", "amp", "the", "year", "last","time", "first", "former",
             "this", "one", "know", "right", "time", "think", "they", "dont","omar", "need", "going", "even", "make"]
stop_words2=["prev","browse, issues", "issue","search","print","help","instructions","archieve", "previous", "next",
             "navigation","page", "arrow", "click", "swipe", "tap", "once", "control", "drag", "thumbnail","facebook","twitter", "google+"
             "gmail","reddit","linkedin","january","date","february","march","april","june","july","august","september","october",
             "november","december", "archive", "manual", "preview" "service" "content-type" "operator" "manual"]
stop_words3=["item","number","short","file","decription","authentic","automotive","service","glass","guide","wheeler","part","item","item","item",
            "book","repair","home","eyeglass","download","best","edition","material","related","life","study","video","share","item","item",
            "post","school","comment","email","read","women","contact","music","webcast","business","report","back","story","item","item","item",
            "free","view","medium","admin","hokder","steel","science","child","rust","show","sport","machine","light","wiley","item","item",
            "owner","game","john","tree","take","change","product","high","answer","sunglass"]

filename = "D:\\MS\\2ndSem\\DIC\\Lab2\\crawlData\\crawl.txt"
with open(filename) as f:
    for line in f:
        word_data = line.lower()
        if(word_data=='\n'):
            with open('D:\\MS\\2ndSem\\DIC\\Lab2\\crawlData\\crawl_filtered.txt', 'a') as val:
                val.write("\n")
        nltk_tokens = nltk.word_tokenize(word_data)
        if(nltk_tokens.__len__()>0):
            wordsFiltered = []
            for w in nltk_tokens:
                w = lemmatizer.lemmatize(w)
                if len(w) > 3 and not w.startswith('http') and not w.startswith('https')and not w.startswith('www')and not w in symbol_list \
                        and not w in stop_words and not w in stop_words1 and not w in stop_words2 and not w in stop_words3 \
                and not w[0].isdigit():
                    wordsFiltered.append(w)

            with open('D:\\MS\\2ndSem\\DIC\\Lab2\\crawlData\\crawl_filtered.txt', 'a') as val:
                for item in wordsFiltered:
                    val.write(item+" ")