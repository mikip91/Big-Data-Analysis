#!/usr/bin/env python

"""mapper_cooccurrence.py"""

import sys

# input comes from STDIN (standard input)
for text in sys.stdin:
    # split the line into paras
    paras = text.split("\n\n")
    for line in paras:
        # change the text to lowercase
        line = line.strip().lower()
        # split the line into words
        words = line.split()

        # increase counters
        for index1 in list(range(0, len(words) - 1)):
            for index2 in list(range(index1, len(words) - 1)):
                if words[index1] != words[index2]:
                    print
                    '%s\t%s' % (str(words[index1] + ',' + words[index2]), 1)