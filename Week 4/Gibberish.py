# Gibberish program
# Author:Georgiana Zugravu C18768301
# Date: 10th October 2019

import string
import math

print("This is Gibberish game\nInsert 2 sets of characters and an word\n"
      "You will receive the word translated in Gibberish language")
play='yes'

while play=='yes' or play=='y':
    first = input("Enter the first Gibberish syllable (add * for the vowel substitute): ")
    second = input("Enter the second Gibberish syllable (* for vowel substitute):")
    word = input("Please enter a word you want to translate: ")
    i = 0
    vowels = "aeiouAEIOU"
    syllable=1
    for i in word :
        if i in vowels :
            print("yeeeesss")
            if syllable == 1:
                word = word[0:word.find(i)] + first + word[word.find(i)+1: len(word)-1]
                syllable = syllable + 1
            else:
                word = word[0:word.find(i)] + second + word[word.find(i) + 1: len(word) - 1]



    print("Your final word: ", word)
    play = input("Play again? (yes/no)")

#def add_syllable()

def  is_digit(syllable):
    return syllable.isdigit()


def asterix(syllable):
    if ord(syllable[0]==42):
        return True
    else:
        return False