# Author: Georgiana Zugravu
# Date: 23rd October 2019
# Compiler: PyCharm




#main
a = [1,2,3]
b = [1,2,3]
c = a

if a == b:
    print("a == b True")
else:
    print("a == b False")

if a is b:
    print("a is b")
else:
    print("a is not b")

if a == c:
    print("a == c True")
else:
    print("a == c False")

if a is c:
    print("a is c")
else:
    print("a is not c")
