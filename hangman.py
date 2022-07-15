#!/usr/bin/python
"""
Created on Fri Jun 24 22:33:10 2022

@author: ege_b
"""

import english_words as ep

import random
from PyDictionary import PyDictionary
dictionary=PyDictionary()


gallow = """
            ____
           |    |
                |
                |
                |
              __|__
                """
first_mistake = """
            ____
           |    |
           0    |
                |
                |
              __|__
"""
second_mistake =  """
            ____
           |    |
           0    |
           |    |
                |
              __|__
"""
third_mistake =  """
            ____
           |    |
           0    |
          /|    |
                |
              __|__
"""
fourth_mistake =  """
            ____
           |    |
           0    |
          /|\   |
                |
              __|__
"""
fifth_mistake =  """
            ____
           |    |
           0    |
          /|\   |
          /     |
              __|__
"""
sixth_mistake =  """
            ____
           |    |
           0    |
          /|\   |
          / \   |
              __|__
"""

progress = []
progress.append(gallow)
progress.append(first_mistake)
progress.append(second_mistake)
progress.append(third_mistake)
progress.append(fourth_mistake)
progress.append(fifth_mistake)
progress.append(sixth_mistake)
alphabet = "abcdefghijklmnopqrstuvwxyz"
#%
prompt = "y"
while prompt == "y":    
    word_bag = list(ep.english_words_lower_set)
    word     = word_bag[random.randint(0,len(word_bag))]
    clue     = dictionary.meaning(word)
    #%
    letters         = []
    guessed_correct = []
    guessed_false   = []
    picked_letters  = []
    for i in word:
        letters.append(i)
        guessed_correct.append("_ ")
    
    for i in range(len(word)):
        spaces = len(word)*"_ "
    
    current = 0
    print("##############################")
    print("Game of Hangman has begun!\n")
    print(spaces)
    print("\n")
    print(progress[current])
    print("##############################")

#%

    while current <6:
        pick = str(input("Pick a letter\n"))
        if pick in picked_letters:
            print("You alredy picked this letter, pick another one")
        elif len(pick) !=1:
            print("Pick a single letter!")
        elif pick not in alphabet:
            print("Pick a lower case letter from the English alphabet:")
            print(alphabet)
        else:    
            picked_letters.append(pick)
        
            if pick in letters:
                print("You guessed right!")
                indices = []
                for i in range(len(letters)):
                    if letters[i] == pick:
                        indices.append(i)
                for j in indices:
                    guessed_correct[j] = pick
            else:
                print("You guessed wrong!")
                current +=1
                guessed_false.append(pick)
            if current >3:
                print("\nDo you need a clue?\nHere is the meaning of the word: ")
                print(clue)
            s = ""
            
            for i in range(len(word)):
                s+=guessed_correct[i] +" "
            print("\nCurrent situation:\n")
            print(s)
            print("\n")
            f = ""
            if len(guessed_false) !=0:
                for j in range(len(guessed_false)):
                    f+=guessed_false[j]+" "
                print(f)
            print(progress[current])
            if current ==6:
                print("You lost!!")
                print("The word was "+ word)
                prompt = input("Do you want to play again? [y/n] ")
                break
            if guessed_correct == letters:
                print("You won, conguratulations!")
                prompt = input("Do you want to play again? [y/n] ")
                break
while True:
    pass