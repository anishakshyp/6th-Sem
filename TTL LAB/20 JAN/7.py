#7.
print("Prime numbers between 10 and 200 are: ")

for n in range(10, 200):
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n)