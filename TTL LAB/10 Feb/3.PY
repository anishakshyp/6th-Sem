#3. WAP to swap the largest and smallest element in a list:

def swap_largest_smallest(lst):
    smallest = min(lst)
    largest = max(lst)
    smallest_index = lst.index(smallest)
    largest_index = lst.index(largest)
    
    lst[smallest_index], lst[largest_index] = lst[largest_index], lst[smallest_index]

my_list = [5, 3, 8, 1, 7]
swap_largest_smallest(my_list)
print("List after swapping:", my_list)
