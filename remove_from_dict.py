#!/usr/bin/env python3

import ast
import sys

def remove(word):
    with open('dict.txt','r') as f:
        words = ast.literal_eval(f.read())
    words.remove(word)
    with open('dict.txt','w') as f:
        f.write(str(words))

if __name__ == "__main__":
    if 2 == len(sys.argv):
        remove(sys.argv[1])
    else:
        print("Usage: python remove_from_dict.py <word_to_remove>")
