# !/usr/bin/env python

import sys
main_list = []
text=["Miki","is", "a" , "nice", "girl" "Miki","is", "a" , "nice", "girl"]
for line in text:
    # remove leading and trailing whitespace
    line = line.lower()

    line = line.strip()

    # Initializing Word List
    pair_word_list = line.split()

    # Storing co-occuring words in list
    for i in range(len(pair_word_list) - 1):
        temp = pair_word_list[i] + " " + pair_word_list[i + 1]
        main_list.append(temp)

    # Sorting the list
    main_list.sort()


# Printing the co-occurring words
for i in range(len(main_list)):
    print("%s\t%s" % (main_list[i], 1))


