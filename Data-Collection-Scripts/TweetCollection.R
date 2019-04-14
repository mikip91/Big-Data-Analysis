# Script for Twitter Data Collection
install.packages("rtweet")
install.packages("qdapRegex")
library("rtweet")
library(stringr)
library(qdapRegex)

#Setup Authentication
create_token(
  app = "Miki_Lab1",
  consumer_key = "JzihmlwTcFf4cxWJsZNWYSGPm",
  consumer_secret = "mn0Axc5BOU87z99tqAnv1IL5V8cc9aahepkaGR6irQPBB2CV9W",
  access_token = "253428076-PVSu508vRLjKXK6MPmP6Iv7ZQoqBMLeavQ5bs7sn",
  access_secret = "GVIkI1heo1CDFNhI97u97l0d35tShORR52CrlzTsoCsrs"
)

#Looking for keyword
tweets <- search_tweets('elections', geocode = lookup_coords("usa"), n=17000, include_rts = FALSE, retryonratelimit = TRUE)
#tweets <- twListToDF(tweets)
tweets <- apply(tweets,2,as.character)
write.csv(tweets, file = "D:/MS/2ndSem/DIC/Lab2/twitterData/NewTweets.csv")

# Reading tweets
OldTweets <- read.csv(file="D:/MS/2ndSem/DIC/Lab2/twitterData/OldTweets.csv", header=TRUE, sep=",")
#OldTweets <- subset(OldTweets, select = -c(X))
OldTweets = OldTweets[,c(-1)]
OldTweets <- apply(OldTweets,2,as.character)
tweets <- merge(OldTweets, tweets, all = TRUE)
tweets <- unique(tweets)
write.csv(tweets, file = "D:/MS/2ndSem/DIC/Lab2/twitterData/OldTweets.csv")

# Writing consolidated tweets again
# tweets <- rbind(OldTweets,tweets)
# tweets = tweets[!duplicated(tweets$id),]
# # tweets = tweets[!duplicated(tweets$text),]
# write.csv(tweets, file = "D:/MS/2ndSem/DIC/Lab2/twitterData/OldTweets.csv")

# Preprocessing tweets
ExistingTweets <- read.csv(file="D:/MS/2ndSem/DIC/Lab2/twitterData/OldTweets.csv", header=TRUE, sep=",")
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
write.table(ProcessedTweets$text, file = "D:/MS/2ndSem/DIC/Lab2/twitterData/tweets.txt", sep="\n\t", col.names = F, row.names = F, quote = F) 
