install.packages('Rcrawler')
library(Rcrawler)
# Reading articles
CollectedArticles <- read.csv(file="D:/MS/2ndSem/DIC/Lab2/NewyorkTimes-Data/OldArticles.csv", header=TRUE, sep=",")
CollectedArticles <- subset(CollectedArticles, select = -c(X))
CollectedUrls = CollectedArticles$web_url

content <- NULL
for(i in c(1:nrow(CollectedArticles)))
{
  Data<-ContentScraper(Url = toString(CollectedUrls[i]),
                       CssPatterns =c(".css-1i2y565"))
  Data<- str_replace_all(Data, "[^[:alnum:]]", " ")
  if(i>1){
    content <- rbind(content, Data)
  }else
  {
    content<- Data
  }
}
content <- content[, 1]
content <- data.frame(content)
cols <- c("text")
colnames(content) <- cols
content <-data.frame(content)
write.table(content$text, file = "D:/MS/2ndSem/DIC/Lab2/NewyorkTimes-Data/articles.txt", sep="\t", col.names = F, row.names = F, quote = F) 
