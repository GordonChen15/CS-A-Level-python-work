#Q4
print("Select one of the following options: ")
print("Enter A for Multiply:")
print("Enter B for Divide: ")
print("Enter C for Add: ")
print("Enter D for Subtract: ")
print("Enter E for Remainder Division: ")
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
operation = str(input("Enter the letter for your chosen operation."))
match operation:
    case "A":
        print(num1*num2)
    case "B":
	    print(num1/num2)
    case "C":
        print(num1+num2)	
    case"D":
	    print(num1-num2)
    case"E":
	    print(num1%num2)

#Q5
Year = int(input("Please input a year"))
LeapYear = False
if Year% 4 == 0:
	LeapYear = True
if Year%100 == 0:
	LeapYear = False
if Year%400 == 0:
	LeapYear = True
if LeapYear:
	print(Year, " is a Leap Year")
else:
	print(Year, "isn’t a Leap Year")
