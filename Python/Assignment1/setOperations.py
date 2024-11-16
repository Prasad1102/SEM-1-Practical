
input_list = [1, 2, 3, 4, 5, 5, 6, 7, 7]
my_set = set(input_list)

print("Original Set:", my_set)

my_set.add(8)
print("After adding 8:", my_set)

my_set.remove(4)
print("After removing 4:", my_set)

my_set.discard(10)
print("After discarding 10:", my_set)

my_set.update([9, 10, 11])
print("After adding multiple elements [9, 10, 11]:", my_set)
