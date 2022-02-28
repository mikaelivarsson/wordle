#!/usr/bin/env python3

from english_words import english_words_set

words = set()

for word in english_words_set:
    if 5 == len(word):
        words.add(word)

with open('dict.txt','w') as f:
    f.write(str(words))
