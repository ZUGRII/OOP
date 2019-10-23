# Author: Georgiana Zugravu
# Date: 22nd October 2019

import copy

list1 = [1,2,99]
list2 = list1
list3 = copy.deepcopy(list2)
list4 = list2
list1 = list1.remove(1)
print(list3)
print(list4)
