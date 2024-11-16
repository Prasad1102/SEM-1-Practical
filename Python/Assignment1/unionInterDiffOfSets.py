# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2

intersection_set = set1 & set2

difference_set = set1 - set2 

symmetric_difference_set = set1 ^ set2

# Print the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
