#!/usr/bin/env python3

from english_words import english_words_lower_alpha_set as words
import ast
import remove_from_dict

def print_menu():
    print(26*"-","Wordle solver",26*"-")
    print("0. Exit")
    print("1. Print unique candidate")
    print("2. Remove words with illegal characters")
    print("3. Remove words without requried characters")
    print("4. Remove words without required character in specific position")
    print("5. Remove words with requried character in wrong position")
    print("6. Remove wrong word")
    print("7. Print candidates")
    print((26+26+len("Wordle solver")+2)*"-")

def remove_illegal(words):
    illegal = input("Input illegal characters: ")
    for c in illegal:
        for word in words.copy():
            if c in word:
                words.remove(word)
    return words

def remove_illegal_character(words, character):
    for word in words.copy():
        if character in word:
            words.remove(word)
    return words

def remove_required(words, required=""):
    if required == "":
        required = input("Input required characters: ")
    for c in required:
        for word in words.copy():
            if c not in word:
                words.remove(word)
    return words

def remove_required_specific(words):
    required = input("Input required character: ")
    position = "5"
    while position not in "01234":
        position = input("Input requried position, 0-4: ")
    for word in words.copy():
        if word[int(position)] != required:
            words.remove(word)
    return words

def remove_required_specific_character(words, character, position):
    for word in words.copy():
        if word[int(position)] != character:
            words.remove(word)
    return words

def remove_required_wrong(words):
    required = input("Input character: ")
    position = "5"
    while position not in "01234":
        position = input("Input wrong position, 0-4: ")
    for word in words.copy():
        if word[int(position)] == required:
            words.remove(word)
    words = remove_required(words, required)
    return words

def remove_required_wrong_character(words, character, position):
    for word in words.copy():
        if word[int(position)] == character:
            words.remove(word)
    words = remove_required(words, character)
    return words

def remove_wrong_word(words):
    word = input("Input wrong word: ")
    words.remove(word)
    remove_from_dict.remove(word)
    return words

def remove_wrong_word_from_words(words, word):
    words.remove(word)
    remove_from_dict.remove(word)
    return words

def print_unique_candidate(words):
    for word in words:
        if 5 == len(set(word)):
            print(word)
            break

def get_unique_candidate(words):
    for word in words:
        if 5 == len(set(word)):
            return word
    return ''

def print_candidates(words):
    print(words)

def main():
    five_letter_words = set()

    with open('dict.txt','r') as f:
        five_letter_words = ast.literal_eval(f.read())

    loop = True
    choice = -1
    while loop:
        print_menu()
        choice = input("Enter choice: ")

        print()
        if choice == "0":
            loop = False
        elif choice == "1":
            print_unique_candidate(five_letter_words)
        elif choice == "2":
            five_letter_words = remove_illegal(five_letter_words)
        elif choice == "3":
            five_letter_words = remove_required(five_letter_words)
        elif choice == "4":
            five_letter_words = remove_required_specific(five_letter_words)
        elif choice == "5":
            five_letter_words = remove_required_wrong(five_letter_words)
        elif choice == "6":
            five_letter_words = remove_wrong_word(five_letter_words)
        elif choice == "7":
            print_candidates(five_letter_words)
        print()

if __name__ == "__main__":
    main()
