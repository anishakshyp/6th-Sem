#3. WAP to check whether a number is a palindrome number or not using a function:

def is_palindrome(num):
    num_str = str(num)
    reversed_num_str = num_str[::-1]
    return num_str == reversed_num_str

number = 121
if is_palindrome(number):
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")