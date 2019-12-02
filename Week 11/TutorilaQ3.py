# Author: Georgiana Zugravu
# Date: 26th November 2019
# Compile: PyCharm
# Python v3.7
# Linear Equation

class LinearEq(object):
    def __init__(self, m, b):
        if (type(m) == str or type(b) == str):
            print("Only rational number allowed")
            m = None
            b = None
        self.m = m
        self.b = b


    def __str__(self):
        return "y = " + str(self.m) + "x + " + str(self.b)

    def __repr__(self):
        pass

    def value(self):
        pass

    def compose(self):
        pass

    def __add__(self, other):
        pass



#Demo Code
a = LinearEq(1,1)
print(a)

b = LinearEq(2, 5)
print(b)

#print(a.compose(b))
#print(a+b)