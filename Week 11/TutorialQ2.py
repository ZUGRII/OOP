#Author: Georgiana Zugravu
#Date: 26th November 2019
#Compile: PyCharm
# Python v3.7


class Whole(object):
    def __init__(self, n = 0):
        if(n < 0):
            print("Negative is not allowed!")
            n = None
        self.N = n

    def __str__(self):
        return str(self.N)

    def __add__(self, b):
        result = self.N + b.N
        if(result < 0):
            print("Result is negative!")
            return None
        return Whole(result)
    def __sub__(self, b):
        result = self.N - b.N
        if (result < 0):
            print("Result is negative!")
            return None
        return Whole(result)

    def __mul__(self, b):
        result = self.N * b.N
        if (result < 0):
            print("Result is negative!")
            return None
        return Whole(result)


#Demo code
A = Whole(4)
B = Whole(2)
C = Whole(-3)

print(A)
print(A + B)
print(A - A)
print(A * B)

#end