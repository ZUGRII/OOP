# Author: Georgiana Zugravu C18768301
# Date: 23rd October 2019
# Compiler: PyCharm

import copy
x = [1,2,3]
y = x
z = copy.deepcopy(x)

print("x is:",x ,"\ny is: ", y, "\nz is: ",z)
x.append(4)
print("\n\n\nx is:",x ,"\ny is: ", y, "\nz is: ",z)