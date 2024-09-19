#Task 1
array = [["Empty"] * 5] * 5
def addname():
    name = str(input("Enter name: "))
    x = int(input("Enter row number of the student: ")) -1
    y = int(input("Enter column number of the student: ")) -1
    array[x][y] = name
    return array

def removename():
    x = int(input("Enter row number of the student: ")) -1
    y = int(input("Enter column number of the student: ")) -1
    array[x][y] = "Empty"
    return array

#Task 2
array = [[0] * 4] * 4
largest = array[0][0]
for i in range(4):
    for j in range(4):
        if array[i][j] > largest:
            largest = array[i][j]
print(largest)

#Task 3
import random
array = [[0] * 6] * 6
largest = array[0][0]
for i in range(6):
    for j in range(6):
        array[i][j] = random.randint(1, 10)

def printrow():
    total = 0
    row = int(input("Enter the row number: "))
    for i in range(6):
        total = total + array[row][i]
    print(total)

def printcol():
    total = 0
    col = int(input("Enter the column number: "))
    for i in range(6):
        total = total + array[i][col]
    print(total)

printrow()

#Task 4
import random

array = [["" for _ in range(3)] for _ in range(3)]
currentplayer = 0

def checkboard(array):
    for i in range(3):
        if array[i][0] == array[i][1] == array[i][2] and array[i][0] != "":
            return array[i][0]
    
    for i in range(3):
        if array[0][i] == array[1][i] == array[2][i] and array[0][i] != "":
            return array[0][i]
    
    if array[0][0] == array[1][1] == array[2][2] and array[0][0] != "":
        return array[0][0]
    elif array[0][2] == array[1][1] == array[2][0] and array[0][2] != "":
        return array[0][2]
    
    return "0"

def print_board(array):
    for row in array:
        print(" | ".join(row))
        print("---------")

for i in range(9):
    x = int(input("Enter the row number: "))
    y = int(input("Enter the column number: "))
    while array[x][y] != "":
        print("The spot is already taken")
        x = int(input("Enter the row number: "))
        y = int(input("Enter the column number: "))
    else:
        if currentplayer == 0:
            array[x][y] = "X"
            currentplayer = 1
        else:
            array[x][y] = "O"
            currentplayer = 0
    
    print_board(array)
    
    if checkboard(array) != "0":
        print("The winner is " + checkboard(array))
        break
else:
    print("The game is a tie")

#Task 5
oldArray = [[""]*3]*3
newArray = [[""]*3]*3
newArray[0][2], newArray[1][2], newArray[2][2] = oldArray[0][0], oldArray[0][1], oldArray[0][2]
newArray[0][1], newArray[1][1], newArray[2][1] = oldArray[1][0], oldArray[1][1], oldArray[1][2]
newArray[0][0], newArray[1][0], newArray[2][0] = oldArray[2][0], oldArray[2][1], oldArray[2][2]
print(newArray)

