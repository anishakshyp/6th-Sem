#6. WAP to find common items in two lists:

def common_items(list1, list2):
    return list(set(list1) & set(list2))

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
result = common_items(list_a, list_b)
print("Common items:", result)
