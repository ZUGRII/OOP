# Functions
# Authors: Georgiana Zugravu
# Date: 17 October 2019
# Compiler: PyCharm


def gcd(bigger, smaller) :
    return bigger % smaller



# main
great = 0
bigger = int(input("Please enter the bigger number: "))
smaller = int(input("Please enter the smaller number: "))
great =  gcd(bigger, smaller)
print("THe greatest common divisor is: ", great)

