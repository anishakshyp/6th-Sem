sample_list = [1, 2, 3, 4, 5]
sample_tuple = (6, 7, 8, 9, 10)
sample_dict = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

sample_list.append(6)
sample_tuple = sample_tuple + (11,)
sample_dict['f'] = 16

sample_list.extend([7, 8])
sample_tuple = sample_tuple + (12, 13)
sample_dict.update({'g': 17, 'h': 18})

sample_list.clear()
sample_tuple = ()
sample_dict.clear()

sample_dict = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
pop_key = 'e'
sample_dict.pop(pop_key, None)

sample_list = [1, 2, 3, 4, 5]
remove_element = 3
sample_list.remove(remove_element)

sample_dict = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
del_key = 'd'
del sample_dict[del_key]

print("List after operations:", sample_list)
print("Tuple after operations:", sample_tuple)
print("Dictionary after operations:", sample_dict)
