# LAB TEST 2 (3D Vector)
# Authors: Georgiana Zugravu C18768301
# Date: 12th of December 2019
# Compiler: PyCharm

import math

class Vector3D (object):
    """Class which stores the coordinates of a 3D vector
            and calculate different operations"""
    def __init__(self, x=0, y=0, z=0):
        """Default constructor, verify the type of the coordinates"""
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, param):
        """Method which calculate the addintion of two vectors"""
        newx = self.x + param.x
        newy = self.y + param.y
        newz = self.z + param.z

        output = str.format('({:0.6f}, {:0.6f}, {:0.6f})', newx, newy, newz)
        return output

    def __sub__(self, param):
        """Method which calculate the subtraction of two vectors"""
        newx = self.x + (param.x*(-1))
        newy = self.y + (param.y*(-1))
        newz = self.z + (param.z*(-1))

        output = str.format('({:0.6f}, {:0.6f}, {:0.6f})', newx, newy, newz)
        return output

    def __mul__(self, param):
        """Metod which calculate the multiplication of
                1. a vector by an integer
                2. two vectors"""
        if type(param) == int or type(param) == float:
            newx = self.x * param
            newy = self.y * param
            newz = self.z * param
            output = str.format('({:0.6f}, {:0.6f}, {:0.6f})', newx, newy, newz)
            return output
        elif type(param) == Vector3D:
            new = self.x*param.x + self.y*param.y + self.z*param.z
            return new

    def magnitude(self):
        """Method which calculate the magnitude of a vector"""
        output = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return output

    def __str__(self):
        """String method, returns the coordinates of the vector"""
        output = str.format('({:0.6f}, {:0.6f}, {:0.6f})',self.x, self.y, self.z )
        return output




# sample call to test the class

# create 2 objects
v1 = Vector3D(1,2,3)
v2 = Vector3D(5,5,5)

print("\nPrinting v1")              # printing first object
print("v1=", v1)

print("\nPrinting v2")              # printing second object
print("v2=", v2)

v3 = v1 + v2
print("\nPrinting addition")        # printing the addition
print("v1+v2 =", v3)

v4 = v1 - v2
print("\nPrinting subtraction")     # printing subtraction
print("v1-v2=", v4)

v5 = v1*v2
print("\nPrinting dot product")     # printing dot product
print("v1*v2=", v5)

v6 = v1*2
print("\nPrinting integer multiplication")  # printing integer multiplication
print("v1*2=", v6)

v7 = v1*2.5
print("\nPrinting integer multiplication")  # printing float multiplication
print("v1*2.5=", v7)

print("\nv1 magnitude is", v1.magnitude())  # printing magnitude