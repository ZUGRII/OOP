# Author: Georgiana Zugravu     C18768301
# Compiler: PyCharm
# Date: 15th October 2019

#exercice 1
import string

def energy ():
    mass = int(input("Please enter the mass: "))
    c = 299792458
    E = mass * c * c
    return E

#exercice 2
def vowels_consonants():
    sentence = input("Enter the sentence: ")
    vowels = "aeiou"
    v_count = 0
    consonants = "bcdfghjklmnpqrstvwxyz"
    c_count = 0
    i = 0
    for i in sentence:
        if i in vowels:
            v_count = v_count + 1
        if i in consonants:
             c_count = c_count + 1
    print("In sentence are ", v_count, " vowels and ", c_count ,"consonants")

#exercice 3
def display_menu ():
    while True:
        print("Chose one of the following:\"
              "1.messaging\
               2.contacts\
               3.games\
               4.settings\
               5.media\
               6.web ")




# main
E = energy()
print("The energy is ", E, " Joules(kg*(m/s)^2) ")
vowels_consonants()
