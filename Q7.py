# Output the largest number in a 2d array using the previous function.

def high_value(my_2d_array):
    Largest = my_2d_array[0][0]
    a = len(my_2d_array)
    for i in range(a):
        b = high_value(my_2d_array[i])
        if b>Largest:
            Largest = b
    #print(Largest) - didn't read question
    return Largest


# This function would also return the location of the largest number in the 2d array.
def high_value(my_2d_array):
    row, col = "",""
    Largest = my_2d_array[0][0]
    a = len(my_2d_array)
    for i in range(a):
        for q in range (len(my_2d_array[i])):
            if my_2d_array[i][q] > Largest:
                Largest = my_2d_array[i][q]
                row = str(i+1)
                col = str(q+1)
    print("The highest value is " + Largest + " at " + row + " " + col)
