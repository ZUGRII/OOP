# Question one from tutorial work sheet
# Author: Georgiana Zugravu
# Date: 21st October 2019
# Compiler: PyCharm

import math

def kaprekar(n):
    if n < 10 :
        return False
    squared_str = str(n*n)

    number1 = 0
    number2 = 0
    for i in range(1, len(squared_str)):

        number1 = int(squared_str[:i])
        number2 = int(squared_str[i:])
        if number1+number2 == n:
            return True

#main function
x = int(input("Enter a top limit (inclusive): "))
print("\nThe list of all Kaprekar numbers from 10 to ",x, "is: " )
for i in range (10, x+1):
    if kaprekar(i):
        print(i, end=" ")
