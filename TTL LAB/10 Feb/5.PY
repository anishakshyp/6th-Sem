#5. WAP to find the second smallest element in a list:

def second_smallest(lst):
    unique_sorted = sorted(set(lst))
    return unique_sorted[1]

my_list = [5, 3, 8, 1, 7]
result = second_smallest(my_list)
print("Second smallest element:", result)
