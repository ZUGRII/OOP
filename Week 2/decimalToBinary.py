#Convert Decimal to Binary
import math
number = input("Enter a number: ")
number_int = int(number)

binary = 0
while(number!=0)
    binary=number%2*10+binary
    number=number/2
print("The number in binary is: " binary)
