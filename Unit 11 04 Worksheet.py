#task 1
def multiples(table, startNum, endNum, pupilName):
    print("Hi", pupilName+ ", this is the table you want.")
    for i in range (startNum, endNum+1):
        print(table, "*", i, "=", table*i)
