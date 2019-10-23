# Functions
# Authors: Georgiana Zugravu
# Date: 17 October 2019
# Compiler: PyCharm

import math

def gcd(bigger, smaller) :
    return math.gcd(bigger, smaller)


def lcm(first, second):
    return (first * second) / gcd(first, second)


def addFrac(frac1, frac2):
    up = (int(frac1[0]) * lcm(int(frac1[2]), int(frac2[2])) / int(frac1[2])) + \
         (int(frac2[0]) *  lcm(int(frac1[2]), int(frac2[2])) /int(frac2[2]))
    frac3 =(up, lcm(int(frac1[2]), int(frac2[2])))
    return frac3


def subFrac(frac1,frac2):
    up = (int(frac1[0]) * lcm(int(frac1[2]), int(frac2[2])) / int(frac1[2])) - (
                int(frac2[0]) * lcm(int(frac1[2]), int(frac2[2])) / int(frac2[2]))
    frac3 = (up, lcm(int(frac1[2]), int(frac2[2])))
    return frac3


def reduce(frac):
    print(frac[0])
    print(frac[2])
    frac = (int(frac[0]) / gcd(int(frac[0]), int(frac[2])) , gcd(int(frac[0]), int(frac[2])))
    return frac


# main
great = 0
bigger = int(input("Please enter the bigger number: "))
smaller = int(input("Please enter the smaller number: "))
great =  gcd(bigger, smaller)
print("THe greatest common divisor is: ", great)

print("\n\n\n")
first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
least = lcm(first, second)
print("The least common multiple is: ", least)

print("\n\n\n")
fraction_one = ()
fraction_two = ()
fraction_one = input("Please enter the fraction numbers followed by comma :")
fraction_two = input("Please enter the fraction numbers followed by comma :")
print(fraction_one)
print(fraction_two)
add = ()
add = addFrac(fraction_one, fraction_two)
print("The sum of the fractions is: ",add)

sub = ()
sub = subFrac(fraction_one, fraction_two)
print("\nThe difference is: ", sub)

print("\n\n\n")
fraction = ()
fraction = input("Please enter the fraction numbers followed by comma :")
r = ()
r = reduce(fraction)
print("Fraction reduce is: ", r)

