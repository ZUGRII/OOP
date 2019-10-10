# Scramble Words program
# eg: hello will become hlelo or hlleo
# Author: Georgiana Zugravu
# C18768301
# Date: 9th October 2019

import random
import string

text_str = input("Type the text to be scrambled and hit enter: ")
words = text_str.split()

i = 0
scramble=''
one_word=''
range_word=''

# scramble each word
for i in range(len(words)):
    one_word = words[i]                                         # take each separate word
        #if ord(i) < 65 or ord(i) > 122:
    range_word = one_word[1:len(one_word)-1]                    # select the range that has to be scrambled
    scramble = range_word[::-1]                                 # scramble the range of the word by reversing it
    words[i]= one_word[0]+scramble+one_word[len(one_word)-1]    # concatenate the pieces

i = 0
text_str = ''
for i in range(len(words)):
    text_str = text_str + words[i] + ' '                        # recreate the sentence

print(text_str)                                                 # print the new sentence
