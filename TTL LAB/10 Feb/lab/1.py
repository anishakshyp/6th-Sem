#1. WAP to find factorial using a function:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = 4
result = factorial(num)
print(f"Factorial of {num} is {result}")