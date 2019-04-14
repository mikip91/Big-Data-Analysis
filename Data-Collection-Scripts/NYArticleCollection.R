# Script for NY Times article collection
# Topic - Politics
# Subtopic - Trump, Administration, government, politics, elections
install.packages("rtimes")
library(rtimes)
Start_Date <- "20190401"
End_Date <- "20190404"

# Setting up authentication 
Sys.setenv(NYTIMES_AS_KEY = "q54vgEeqyyr2xPubZrlsK0PBkAyDzJN1")

# Collecting articles
NYDataframe <- as_search(q = "elections", begin_date = Start_Date, end_date = End_Date, sleep=20, all_results = TRUE)
NYDataframe <- NYDataframe$data
NYDataframe <- subset(NYDataframe, select = -c(multimedia, keywords, byline.person))
NYDataframe = NYDataframe[!duplicated(NYDataframe$`_id`),]
NYDataframe = NYDataframe[!duplicated(NYDataframe$snippet),]
NYDataframe = NYDataframe[!duplicated(NYDataframe$word_count),]
write.csv(NYDataframe, file = "D:/MS/2ndSem/DIC/Lab2/newsData/elections.csv")

# Reading Articles
Articles <- read.csv(file="D:/MS/2ndSem/DIC/Lab2/newsData/elections.csv", header=TRUE, sep=",")
Articles <- subset(Articles, select = -c(X))
names(Articles)[11] <- "_id"

# Writing consolidated Articles again
Articles <- rbind(Articles,NYDataframe)
Articles = Articles[!duplicated(Articles$`_id`),]
Articles = Articles[!duplicated(Articles$snippet),]
Articles = Articles[!duplicated(Articles$word_count),]
write.csv(Articles, file = "D:/MS/2ndSem/DIC/Lab2/newsData/elections.csv")


