#Write a program which prompts the user for a string and outputs the same string but with the first and last character exchanged.
a = str(input("Type a string"))
#a[0], a[len(a)-1] = a[len(a)-1], a[0] (but chr in strings cannot be assigned)
print(a[len(a)-1]+a[1:len(a)-1]+a[0])
