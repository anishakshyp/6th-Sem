#4.
x = input("Enter the first number: ")
y = input("Enter the second number: ")
z = input("Enter the third number: ")

if x < y:
    if x < z:
        min = x
    else:
        min = z
else:
    if y < z:
        min = y
    else:
        min = z

if x > y:
    if x > z:
        max = x
    else:
        max = z
else:
    if y > z:
        max = y
    else:
        max = z

if x != min and x != max:
    middle = x
elif y != min and y != max:
    middle = y
else:
    middle = z

print("Minimum is", min)
print("Maximum is", max)
print("Middle element is", middle)