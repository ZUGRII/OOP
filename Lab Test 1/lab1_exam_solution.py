def make_new_row(old_row):
    """Requires:
       -- list old_row that begins and ends with a 1 and has zero or more
          integers in between (has to have at least [1,1])
          special cases are [] and [1]
       Returns:
       -- list beginning and ending with a 1 and each interior (non 1)
          integer is the sum of the corresponding old_row elements
          For example if old_row = [ 1,4,6,4,1], then new_row = [1,5,10,10,5,1],
          i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1
          special cases [] returns [1] and [1] returns [1,1]"""
    # part B
    if old_row == []:
        return [1]
    if old_row == [1]:
        return [1,1]

    # part A
    new_row = [1]
    for i in range(len(old_row)-1):
        new_row.append(old_row[i] + old_row[i+1])
    else:
        new_row.append(1)
    return new_row

n_str = input("Enter the desired height of Pascal's triangle (n > 2): ")

while True:
    try:
        # Convert string to int
        n = int(n_str)
    except:
        # Not a number. Ask a new input
        n_str = input("Only integers accepted. Please enter again: ")
    else:
        if n > 2:
            # If number is greater than 2 break loop and accept input
            break
        else:
            n_str = input("Only numbers greater than 2 accepted. Please enter again: ")

L = [[1]]
r = [1,1]
for i in range(n-2):
    L.append(r)
    r = make_new_row(r)
else:
    L.append(r)

print("Printing whole list of lists:")
print(L)

print("Printing list of lists, one list at a time:")
for i in L:
    print(i)

# Printing triangle as string
print("Printing lists as strings")
for i in L:
    row = ' '.join([str(j) for j in i])
    print(row.center(100))
