# Gibberish program
# Authors: Georgiana Zugravu C18768301 + Yecenia Gonzalez C18738429
# Date: 10th October 2019
# This is the gibberish game, this program allows a user to insert two "gibberish" (eg.'pi','ru'se') that will be use in
# a word, also inserted by the user, to translate it from english to "gibberish". The user can use a wildcard (*) that
# can only appear at the beginning of the syllable.


# Generate funtion 'is_digit'
# This will check if the input 'gibberish'is an alphabet letter
def is_digit(syllable):
    i = 0
    check = False
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*"
    for i in range(0, len(syllable)):

        if syllable[i] not in alfabet:
            print("Syllable must only contain letters or a wildcard :'*'\nTry again!")
            check = True

    return check


# Generate function 'asterix'
# This function will check if the inputted 'gibberish' is the wildcard character (*)
def asterix(syllable):
    if ord(syllable[0]) == 42:
        return 1
    else:
        return 0


# Generate function 'add_syllable'
# This function will contain the translated word
def add_syllable(new, syllable):
    new = new + syllable
    return new

# Game intro
print("\n\n\nThis is Gibberish game!\nYou will need to insert 2 sets of characters and a word\n"
      "You will get the word translated in Gibberish language !\n"
      "Let's play!")
play = 'yes'

# Prompt user for input
while play == 'yes' or play == 'y':
    check = True
    while check:
        first = input("Please enter the first Gibberish syllable (add * for the vowel substitute): ")
        check = is_digit(first)
    check = True
    while check:
        second = input("Please enter the second Gibberish syllable (* for vowel substitute):")
        check = is_digit(second)

# Initialize variables
    word = input("Please enter a word you want to translate: ")
    i = 0
    vowels = "aeiouAEIOU"
    syllable = 1
    new_word = ''
    check_asterix = 0

# word check
    for i in range(0, len(word)):  # for loop to check each letter of the word
        if word[i] in vowels:  # checks if the letter at index position (i) is a vowel
            if syllable == 1:  # checks the first vowel
                if asterix(first):  # stores first vowel to use as the wildcard
                    first = word[i] + first[1: len(first)]

                new_word = add_syllable(new_word, first)
                syllable = syllable + 1 # change value as 'syllable' to stop the if statement

            else:
                if word[i - 1] not in vowels:  # if previous letter is not a vowel
                    check_asterix += asterix(second)
                    if check_asterix != 0:  # stores second vowel to use as the wildcard
                        second = word[i] + second[1:len(second)]
                    new_word = add_syllable(new_word, second)

        new_word = new_word + word[i] # add each letter of the input word to the new word

    print("Your final word is : ", new_word)  # Print out resulting word
    check_play = True
    while check_play :
        play = input("Play again? (yes/no)")  # Ask user to play again
        if play == "yes" or play == "no" or play == "n" or play == "y" :  # check the input
            check_play = False
        else :
            print("Please enter y to continue or n to quit: ")

print("Thank you for playing!")
