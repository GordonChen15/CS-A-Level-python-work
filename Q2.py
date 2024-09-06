#Write a program that has three prompts for the user to enter the current time. The first will be the hours (12 hr clock), the second will be the minutes and the third will be either am or pm.
hour = int(input("Current hour?"))
min = int(input("Current minute?"))
apm = str(input("am or pm?"))
if hour == 12:
    hour = 0
if apm == "am":
    print(hour*60+min)
elif apm == "pm":
    print((hour+12)*60+min)
