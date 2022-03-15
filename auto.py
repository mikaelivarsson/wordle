#!/usr/bin/env python3

import pyautogui
import wordle
import ast
import time

green = (83,141,78)
yellow = (181,159,59)

q = pyautogui.locateOnScreen('q.png', confidence=0.9)
print("q: ",q)
pyautogui.moveTo(q.left, q.top)
pyautogui.click()

words = set()
with open('dict.txt','r') as f:
    words = ast.literal_eval(f.read())

foundAnswer = False

for row in range(6):
    while not foundAnswer:
        print("")
        if foundAnswer:
            break
        guess = wordle.get_unique_candidate(words)
        if guess == '':
            guess = words.pop()
        pyautogui.write(guess+'\n')
        time.sleep(0.2)
        if not pyautogui.locateOnScreen('notinlist.png') and not pyautogui.locateOnScreen('notenough.png'):
            foundAnswer = True
            time.sleep(2)
            if not pyautogui.locateOnScreen('statistics.png'):
                im = pyautogui.screenshot()
                for col, char in enumerate(guess):
                    if im.getpixel((q.left+100+col*67, q.top-480+row*67)) == green:
                        # correct position
                        words = wordle.remove_required_specific_character(words, char.lower(), col)
                        print("Green\t",char)#," ",q.left+100+col*67,",",q.top-480+row*67)
                    elif im.getpixel((q.left+100+col*67, q.top-480+row*67)) == yellow:
                        # correct character, wrong position
                        words = wordle.remove_required_wrong_character(words, char.lower(), col)
                        print("Yellow\t",char)#," ",q.left+100+col*67,",",q.top-480+row*67)
                        foundAnswer = False
                    else:
                        # wrong character
                        words = wordle.remove_illegal_character(words, char.lower())
                        print("Wrong\t",char)#," ",q.left+100+col*67,",",q.top-480+row*67)#," Avläst: ",im.getpixel((q.left+100+col*67,q.top-480+row*67)))
                        foundAnswer = False
            else:
                foundAnswer = True
            break
        if not foundAnswer:
            words = wordle.remove_wrong_word_from_words(words, guess)
            for _ in range(5):
                pyautogui.press('backspace')
            print("removed ",guess)
print("")
print("Correct word: "+guess)
