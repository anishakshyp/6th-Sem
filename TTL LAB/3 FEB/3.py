# 3. Print all Armstrong numbers between 1 to 1000

armstrong_numbers = [num for num in range(1, 1001) if num == sum(int(digit) ** len(str(num)) for digit in str(num))]
print("Armstrong numbers between 1 and 1000:", armstrong_numbers)
