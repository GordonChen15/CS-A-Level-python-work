#Write a program which prompts the user for a string and outputs the same string but with the first and last character exchanged.
a = str(input("Type a string"))
print(a[len(a)-1]+a[1:len(a)-1]+a[0])
