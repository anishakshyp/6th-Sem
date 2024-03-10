#3.
print("Convert Temperature")
choice = input("Enter C to convert Fahrenheit to Celsius else F to convert Celsius to Fahrenheit: ")

if choice == 'C' or choice == 'c':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "Fahrenheit = ", celsius, "Celsius")

elif choice == 'F' or choice == 'f':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(celsius, "Celsius = ", fahrenheit, "Fahrenheit")

else:
    print("Invalid choice")