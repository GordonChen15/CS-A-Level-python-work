# The average of non-negative numbers entered.
count, total = 0, 0
a = int(input("Enter a number: "))
while a >= 0:
    count += 1
    total += a
    a = int(input("Enter a number: "))
print(total, count)
