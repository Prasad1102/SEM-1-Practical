def remove_item_from_tuple(input_tuple, item_to_remove):
    temp_list = list(input_tuple)
    
    if item_to_remove in temp_list:
        temp_list.remove(item_to_remove)
    
    return tuple(temp_list)

# Example usage:
input_tuple = (1, 2, 3, 4, 5, 6)
item_to_remove = 4

result = remove_item_from_tuple(input_tuple, item_to_remove)

print("Original Tuple:", input_tuple)
print("Tuple after removing item:", result)
