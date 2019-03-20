# Script for Twitter Data Collection
install.packages("twitteR")
install.packages("qdapRegex")
library("twitteR")
library(stringr)
library(qdapRegex)

#Setup Authentication
setup_twitter_oauth("JzihmlwTcFf4cxWJsZNWYSGPm", 
                    "mn0Axc5BOU87z99tqAnv1IL5V8cc9aahepkaGR6irQPBB2CV9W", 
                    "253428076-PVSu508vRLjKXK6MPmP6Iv7ZQoqBMLeavQ5bs7sn", 
                    "GVIkI1heo1CDFNhI97u97l0d35tShORR52CrlzTsoCsrs")
# Collecting tweets
Start_date <- "2019-03-01"
End_date <- "2019-03-19"
tweets <- searchTwitter('Trump Administration', n=100, lang="en", since=Start_date, until=End_date)
tweets <- twListToDF(tweets)
write.csv(tweets, file = "D:/MS/2ndSem/DIC/Lab2/Twitter-Data/NewTweets.csv")

# Reading tweets
OldTweets <- read.csv(file="D:/MS/2ndSem/DIC/Lab2/Twitter-Data/OldTweets.csv", header=TRUE, sep=",")
OldTweets <- subset(OldTweets, select = -c(X))

# Writing consolidated tweets again
tweets <- rbind(OldTweets,tweets)
tweets = tweets[!duplicated(tweets$id),]
# tweets = tweets[!duplicated(tweets$text),]
write.csv(tweets, file = "D:/MS/2ndSem/DIC/Lab2/Twitter-Data/OldTweets.csv")

# Preprocessing tweets
ExistingTweets <- read.csv(file="D:/MS/2ndSem/DIC/Lab2/Twitter-Data/OldTweets.csv", header=TRUE, sep=",")
ExistingTweets = ExistingTweets[!duplicated(ExistingTweets$text),]
ProcessedTweets <- data.frame(iconv(ExistingTweets$text, "latin1", "ASCII", sub=""))
# Removing urls
ProcessedTweets <- rm_url(ProcessedTweets$iconv.ExistingTweets.text...latin1....ASCII...sub......)
# Removing hashtags and mentions
ProcessedTweets <- sub('#\\w+|@\\w+',' ', ProcessedTweets)
ProcessedTweets <- data.frame(gsub("RT","", ProcessedTweets))
ProcessedTweets <- data.frame(gsub("[^[:alnum:]]", " ", ProcessedTweets$gsub..RT.......ProcessedTweets.))
cols <- c("text")
colnames(ProcessedTweets) <- cols
write.table(ProcessedTweets$text, file = "D:/MS/2ndSem/DIC/Lab2/Twitter-Data/tweets.txt", sep="\t", col.names = F, row.names = F, quote = F) 
