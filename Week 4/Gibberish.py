# Gibberish program
# Author:Georgiana Zugravu C18768301 +
# Date: 10th October 2019

import string
import math

def is_digit(syllable):
    i = 0
    check = False
    for i in range(0, len(syllable)):

        if ord(syllable[i]) < 65 or ord(syllable[i]) > 122 or ord(syllable) != 42 :
            print("Syllable must only contain letters or a wildcard :'*'\nTry again!")
            check = True

    return check


def asterix(syllable):
    if ord(syllable[0]) == 42:
        return True
    else:
        return False

def add_syllable(new, syllable):
    new = new + syllable
    return new


print("This is Gibberish game\nInsert 2 sets of characters and an word\n"
      "You will receive the word translated in Gibberish language")
play='yes'

while play=='yes' or play=='y':
    check = True
    while check :
        first = input("Enter the first Gibberish syllable (add * for the vowel substitute): ")
        check = is_digit(first)
    check = True
    while check:
        second = input("Enter the second Gibberish syllable (* for vowel substitute):")
        check = is_digit(second)

    word = input("Please enter a word you want to translate: ")
    i = 0
    vowels = "aeiouAEIOU"
    syllable = 1
    new_word = ''

    for i in range(0, len(word)):
        if word[i] in vowels :

            if syllable == 1:

                if asterix(first):
                    first = word[i] + first[1: len(first)]
                new_word = add_syllable(new_word, first)

                syllable = syllable + 1
            else:
                if word[i-1] not in vowels :
                    if asterix(second):
                        second = word[i] + second[1:len(second)]
                    new_word = add_syllable(new_word, second)


        new_word = new_word + word[i]



    print("Your final word: ", new_word)
    play = input("Play again? (yes/no)")
