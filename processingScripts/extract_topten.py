import pandas as pd
## Code for extracting top 12 from tweets
#data=pd.read_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\twCount.txt", sep='\t', encoding='ISO-8859-1')
data=pd.read_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\crawlco.txt", sep='\t', encoding='ISO-8859-1')
data.columns=['Word', 'Count']
data=data.sort_values('Count', ascending=False)
print(data)
top_ten_data=data[0:10]
top_ten_data.reset_index(drop = True, inplace = True)
#top_ten_data.to_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\top_50_tweets.txt",sep='\t',header=False, index=False)
top_ten_data.to_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\top_10_crawlco.txt",sep='\t',header=False, index=False)


## Code for extracting top 12 from nytimes
#data=pd.read_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\nyCount.txt", sep='\t', encoding='ISO-8859-1')
data=pd.read_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\crawlco.txt", sep='\t', encoding='ISO-8859-1')
data.columns=['Word', 'Count']
data=data.sort_values('Count', ascending=False)
print(data)
top_ten_data=data[0:200]
top_ten_data.reset_index(drop = True, inplace = True)
#top_ten_data.to_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\top_10_ny.txt",sep='\t',header=False, index=False)
top_ten_data.to_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\top_200_crawlco.txt",sep='\t',header=False, index=False)