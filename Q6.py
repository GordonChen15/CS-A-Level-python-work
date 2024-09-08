# Write a procedure to output the highest value in the array.

def high_value(my_array):
    highest = my_array[0]
    for i in range(len(my_array)):
        if my_array[i] > highest:
            highest = my_array[i]
    print(highest)
