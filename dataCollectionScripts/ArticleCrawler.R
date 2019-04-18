install.packages('Rcrawler')
library(Rcrawler)
library(stringr)
# Reading articles
CollectedArticles <- read.csv(file="D:/MS/2ndSem/DIC/Lab2/newsData/elections.csv", header=TRUE, sep=",")
CollectedArticles <- subset(CollectedArticles, select = -c(X))
CollectedUrls = CollectedArticles$web_url

content <- NULL
for(i in c(1:140))
{
  Data<-ContentScraper(Url = toString(CollectedUrls[i]),
                       CssPatterns =c(".css-1i2y565"))
  if(!is.na(Data)){
    Data<- str_replace_all(Data, "[^[:alnum:]]", " ")
    if(i>1){
      content <- rbind(content, Data)
    }else
    {
      content<- Data
    }
  }
  else{
    content<- ""
  }
}
content <- paste(content, "\n")
#content <- content[, 1]
content <- data.frame(content)
cols <- c("text")
colnames(content) <- cols
content <-data.frame(content)
write.table(content$text, file = "D:/MS/2ndSem/DIC/Lab2/newsData/newsDataOutput/elections.txt", sep="\n\t", col.names = F, row.names = F, quote = F) 
