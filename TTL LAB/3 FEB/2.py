# 2. Sum of all the digits present in an n-digit number:

n_digit_number = int(input("Enter an n-digit number: "))
digit_sum = sum(int(digit) for digit in str(n_digit_number))
print(f"Sum of digits: {digit_sum}")
