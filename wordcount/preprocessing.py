#!/usr/bin/env python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
stop_words=set(stopwords.words("english"))
symbol_list=['.',',','?','!', '@', '"', "'", '<', '>', '/', '[', ']','{','}','(',')',':',';', '…', '”', '#','$','%','^','&','*','-','+','_','=']
stop_words1=["said", "also", "like", "could", "also", "would" ,"us", "want", "via", "amp"]

file = pd.read_csv("D:\MS\2ndSem\DIC\Lab2\twitterData\politics.txt", sep='\n')
firstCol = np.asarray(file.FirstColName)
print(firstCol)
