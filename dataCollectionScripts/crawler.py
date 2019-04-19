import warc
import wget
from langdetect import detect

# prefix= "https://commoncrawl.s3.amazonaws.com/"
# exurl ="crawl-data/CC-MAIN-2019-13/segments/1552912202658.65/warc/CC-MAIN-20190322115048-20190322141048-00227.warc.gz"
# finalurl= prefix+exurl
# finalurl = finalurl.replace('/warc/','/wet/').replace('.warc.','.warc.wet.')
# wget.download(exurl)

keywords= 'trump' or 'president' or 'government' or 'party' or 'people' or 'election' or 'state' or 'house' or 'political' \
          or 'politics' or 'republican' or 'vote' or 'administration'
count = 0
# exurl ="https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-13/segments/1552912202658.65/wet/CC-MAIN-20190322115048-20190322141048-00227.warc.wet.gz"
exurl2 ="https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-13/segments/1552912203021.14/wet/CC-MAIN-20190323201804-20190323223804-00227.warc.wet.gz"
exurl3 ="https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-13/segments/1552912201672.12/wet/CC-MAIN-20190318191656-20190318213656-00398.warc.wet.gz"

# wget.download(exurl)
records = warc.open("D:\MS\\2ndSem\DIC\Lab2\\crawlData\\text.warc.wet")
newfile = open("D:\\MS\\2ndSem\\DIC\\Lab2\\crawlData\\crawl2.txt",'a')
for record in records:
    url = record.header.get('WARC-Target-URI', None)
    if url:
        text = record.payload.read()
        try:
            if (count<520 and detect(text.decode("utf-8")) == 'en'):
                if keywords in text.decode("utf-8").lower():
                    newfile.write(str(text, 'utf-8'))
                    newfile.write('\n\n')
                    count = count+1
                    print(count)
        except Exception:
            pass
