def separate_digits(input_list):
    digits_list = [item for item in input_list if str(item).isdigit()]
    return digits_list

original_list = ['a', 1, 'b', 3, 'c', 5, 'd', 2]
digits_list = separate_digits(original_list)

print("Original List:", original_list)
print("List of Digits:", digits_list)
