# Functions
# Authors: Georgiana Zugravu
# Date: 17 October 2019
# Compiler: PyCharm


def gcd(bigger, smaller) :
    if(bigger> smaller):
        if (bigger % smaller == 0):
            return smaller
        else:
            return bigger % smaller
    else:
        if(smaller % bigger == 0):
            return bigger
        else:
            return smaller % bigger
def lcm(first, second):
    great = gcd(first, second)
    return (first * second ) / gcd(first, second)



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