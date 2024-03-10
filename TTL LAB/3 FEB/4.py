# 4. Input an integer, reverse it, and check whether it is a palindrome

input_integer = int(input("Enter an integer: "))
reversed_integer = int(str(input_integer)[::-1])
print(f"Reversed integer: {reversed_integer}")
print(f"Is it a palindrome? {'Yes' if str(input_integer) == str(input_integer)[::-1] else 'No'}")
