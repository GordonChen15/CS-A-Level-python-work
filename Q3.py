#Write a program that prompts the user for an integer representing the number of minutes that have passed since midnight.

printh = ""
printm = ""
min = int(input("Number of minutes passed since midnight?"))
hour = min//60
min2 = min%60
if hour <10:
    printh = "0"+str(hour)
else:
    printh = str(hour)
if min2<10: 
    printm = "0"+str(min2)
else:
    printm = str(min2)
print(printh+":"+printm)
