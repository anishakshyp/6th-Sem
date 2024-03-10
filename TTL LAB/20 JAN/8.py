#8.
sum = 0

while True:
    n= input("Enter a number:")
    
    if n.lower() == "done":
        break

    try:
        n = float(n)
        sum += n
    except ValueError:
        print("Invalid input. Enter a valid number.")

print("The total sum is:", sum)