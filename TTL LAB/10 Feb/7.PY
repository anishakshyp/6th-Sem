#7. WAP to swap pairs of elements in a list:

def swap_pairs(lst):
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]

list = [1, 2, 3, 4, 5, 6]
swap_pairs(list)
print("List after the pairs are swapped:", list)
