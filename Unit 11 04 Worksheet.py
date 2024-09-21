#task 1
def multiples(table, startNum, endNum, pupilName):
    print("Hi", pupilName+ ", this is the table you want.")
    for i in range (startNum, endNum+1):
        print(table, "*", i, "=", table*i)
#task 2 q3
def getPword (attempt):
    password = ""
    if attempt == 1:
        password = str(input("Enter password"))
        while len(password) < 6 or len(password) > 8:
            print("Error. Password must be between 6 to 8 characters long.")
            password = str(input("Enter password"))
    elif attempt == 2:
        password = str(input("Enter password again"))
        while len(password) < 6 or len(password) > 8:
            print("Error. Password must be between 6 to 8 characters long.")
            password2 = str(input("Enter password"))
    return password

#task 2 q4
def emptyCarPark (park):
    for i in range(10):
        for j in range(6):
            park[i][j] = "empty"
    return park

def parkACar (park):
    plate = str(input("Enter car plate: "))
    row = int(input("Enter row in thich the car is parked: "))
    col = int(input("Enter column in thich the car is parked: "))
    if park[row][col] == "empty":
        park[row][col] = plate
    else:
        print("The spot is already occupied.")
        row = int(input("Enter row in thich the car is parked: "))
        col = int(input("Enter column in thich the car is parked: "))
    return park

def removeACar (park):
    plate = str(input("Enter car plate: "))
    for i in range(10):
        for j in range(6):
            if park[i][j] == plate:
                park[i][j] = "empty"
    return park

def displayCarParkGrid (park):
    for row in park:
            print(row)
