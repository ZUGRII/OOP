# LAB TEST 2
# Authors: Georgiana Zugravu C18768301
# Date: 12th of December 2019
# Compiler: PyCharm

import math

class Vector3D (object):
    """Class which stores the coordinates of a 3D vector
            and calculate different operations"""
    def __init__(self, x=0, y=0, z=0):
        """Default constructor, verify the type of the coordinates"""

        if type(x) == int or type(x) == float:
            self.x = float(x)

        self.y = float(y)
        self.z = float(z)

    def __add__(self, param):
        """Method which calculate the addintion of two vectors"""
        newx = self.x + param.x
        newy = self.y + param.y
        newz = self.z + param.z

        output = str.format('{:0.6f}, {:0.6f}, {:0.6f}', newx, newy, newz)
        return output

    def __sub__(self, param):
        """Method which calculate the subtraction of two vectors"""
        newx = self.x + (param.x*(-1))
        newy = self.y + (param.y*(-1))
        newz = self.z + (param.z*(-1))

        output = str.format('{:0.6f}, {:0.6f}, {:0.6f}', newx, newy, newz)
        return output
        #return self.__sub__()

    def __mul__(self, param):
        """Metod which calculate the multiplication of
                1. a vector by an integer
                2. two vectors"""
        if type(param) == int:
            newx = self.x * param
            newy = self.y * param
            newz = self.z * param

            output = str.format('{:0.6f}, {:0.6f}, {:0.6f}', newx, newy, newz)
            return output

        else:
            new = self.x*param.x + self.y*param.y + self.z*param.z
            return new

    def magnitude(self):
        """Method which calculate the magnitude of a vector"""
        output = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return output

    def __str__(self):
        """String method, returns the coordinates of the vector"""
        output = str.format('{:0.6f}, {:0.6f}, {:0.6f}',self.x, self.y, self.z )
        return output




# sample call to test the class

v1 = Vector3D(1,2,3)
v2 = Vector3D(5,5,5)

print("Printing v1")
print("v1=", v1)

print("Printing v2")
print("v2=", v2)

v3 = v1 + v2
print("Printing addition")
print("v1+v2 =", v3)

v4 = v1 - v2
print("Printing subtraction")
print("v1-v2=", v4)

print("Printing dot product")
v5 = v1*v2
print("v1*v2=", v5)

print("Printing integer multiplication")
v6 = v1*2
print("v1*2=", v6)

print("v1 magnitude is", v1.magnitude())