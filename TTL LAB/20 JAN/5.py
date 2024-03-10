#5.
n = int(input("Enter a number between 0 and 999: "))

if n >= 0 and n <= 9:
    print(n, "is a single digit number.")

elif n >= 10 and n <= 99:
    print(n, "is a double digit number.")

elif n >= 100 and n <= 999:
    print(n, "is a three digit number.")

else:
    print(n, "is not in 0-999 range")
