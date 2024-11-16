# Creating a dictionary
my_dict = {
    1: "apple",
    2: "banana",
    3: "cherry",
    4: "date",
    5: "elderberry"
}

search_key = 3
if search_key in my_dict:
    print(f"Item found: Key {search_key} has value '{my_dict[search_key]}'")
else:
    print(f"Item not found for Key {search_key}")

odd_elements = {key: value for key, value in my_dict.items() if key % 2 != 0}
print("Odd elements in the dictionary:", odd_elements)
