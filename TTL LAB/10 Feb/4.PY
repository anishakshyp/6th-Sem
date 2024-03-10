#4. WAP to remove duplicate elements in a list:

def remove_duplicates(lst):
    return list(set(lst))

my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(my_list)
print("List after removing duplicates:", result)
