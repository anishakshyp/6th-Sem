# 1. Print Fibonacci series up to nth term (user input):

n = int(input("Enter the value of n: "))
fib_series = [0, 1]
while len(fib_series) < n:
    fib_series.append(fib_series[-1] + fib_series[-2])
print(f"Fibonacci series up to {n} terms: {fib_series}")
