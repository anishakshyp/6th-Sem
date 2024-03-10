#4. WAP to find GCD using a function:
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 16
num2 = 24
result = find_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")