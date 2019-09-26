#Convert Decimal to Binary
#Author: Georgiana Zugravu
#Date: 26th September 2019
#Compiler: PyCharm

import math

number = input("Enter a number: ")
number_int = int(number)

if(number_int<0):
    print("The number is negative")
else:
    print("The number in binary is: ", bin(number_int))
