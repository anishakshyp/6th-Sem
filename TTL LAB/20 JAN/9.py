#9.
num = int(input("Enter a number between 100 and 150: "))

while True:
    flag = 0

    for i in range(2, num):
        if (num % i) == 0:
            flag = 1
            break

    if flag == 0:
        print(num)
        break

    num += 1

print("Loop terminated at prime number", num)