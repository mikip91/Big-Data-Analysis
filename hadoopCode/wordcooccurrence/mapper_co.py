#!/usr/bin/env python
import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.lower()
    line = line.strip()
    # Initializing Word List
    words = line.split()

    for i in range(len(words) - 1):
        if not (words[i][0].isdigit()):
            for j in range(i + 1, len(words)):
                if not (words[j][0].isdigit()):
                    print ("%s|%s\t%s" % (words[i], words[j], 1))