#!/usr/bin/env python
import sys

for line in sys.stdin:
    wordlist= ["trump","election", "politics","people","vote","president","democrat", "american", "state", "party"]
    # remove leading and trailing whitespace
    line = line.lower()
    line = line.strip()
    # Initializing Word List
    words = line.split()

    for i in range(len(words) - 1):
        if words[i] in wordlist and not (words[i][0].isdigit()):
            for j in range(i + 1, len(words)):
                if not (words[j][0].isdigit()) and not words[i]==words[j]:
                    if (words[i] < words[j]):
                        word1 = words[i]
                        word2 = words[j]
                    else:
                        word1 = words[j]
                        word2 = words[i]
                    print ("%s|%s\t%s" % (word1, word2, 1))