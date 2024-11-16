def tuple_operations(input_tuple):
    tuple_length = len(input_tuple)

    max_element = max(input_tuple)
    min_element = min(input_tuple)

    avg = sum(input_tuple) / tuple_length

    sorted_tuple = tuple(sorted(input_tuple))

    return tuple_length, max_element, min_element, avg, sorted_tuple

input_tuple = (10, 20, 30, 40, 50)

length, maximum, minimum, average, sorted_tuple = tuple_operations(input_tuple)

print("Tuple:", input_tuple)
print("Length of tuple:", length)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
print("Average of elements:", average)
print("Sorted tuple:", sorted_tuple)
