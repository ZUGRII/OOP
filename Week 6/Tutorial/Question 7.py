# Author: Georgiana Zugravu C18768301
# Date: 23rd October 2019
# Compiler: PyCharm

listA = [10,20,30,40,50]
listB = []
length = len(listA)

for i in range(0, length):
    if i == length-1:
        listB.append(listA[i-1]+listA[i])
    elif i == 0:
        listB.append(listA[i] + listA[i + 1])
    else:
        listB.append(listA[i - 1] + listA[i] + listA[i + 1])

print(listA)
print(listB)