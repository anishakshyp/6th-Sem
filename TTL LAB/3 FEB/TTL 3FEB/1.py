def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [n for n in range(101) if is_prime(n)]
print("Prime numbers in the range 0 to 100:", prime_numbers)