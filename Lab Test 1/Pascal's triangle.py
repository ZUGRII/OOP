# Pascal's triangle program
# Authors: Georgiana Zugravu C18768301
# Date: 24 October 2019
# Compiler: PyCharm

# Function make_new_row
# This funtion generate a new row based on the previous one
def make_new_row (old_row):
    """This function generates a new row based on the previous one/
                It creates Pascal's Triangle"""
    if old_row == []:                                       # if the list is empty
        new_row = [1]                                       # new list is [1]
    elif old_row == [1]:                                    # if the old list is [1]
        new_row = [1,1]                                     # new list is [1,1]
    else:
        new_row = [1,]                                      # creates the new list
        for i in range(1, len(old_row)):
            new_row.append(old_row[i-1] + old_row[i])       # fill the list
        new_row.append(1)                                   # append 1 at the end of the row

    return new_row                                           # return the new row


#main function
old_row = []
L = []            #list of lists
try:                                                                        # Check user's input
    height = int(input ("Enter the desired height of Pascal's triangle: ")) # prompt for the input
except ValueError:
    print("Please enter an integer.")                                       # inform the user that the input is not valid
    height = int(input("Enter the desired height of Pascal's triangle: "))  # prompt again for the input


for i in range(0, height):                       # create list of lists
    old_row = make_new_row(old_row)              # call function make_new_row
    L.append(old_row)                            # append the new row to the list of lists


print("Printing whole list of lists:\n", L)      # print the lists on one line


print("\nPrinting list of lists, one list at a time: ")
for i in L:
    print(i)                                    # print the lists on separate lines


print("\n\nPrinting Pascal's triangle:")
for j in range(0, len(L)):                      # create Pascal's triangle

    print(' '.join([str(i) for i in L[j]]).center(100))   # display each list as a string centred in the middle, with the width 100
    print("\n")