# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

print("Original Dictionary:", my_dict)

my_dict["email"] = "john@example.com"
print("After adding 'email':", my_dict)

del my_dict["city"]
print("After removing 'city':", my_dict)

popped_value = my_dict.pop("age")
print("After popping 'age':", my_dict)
print("Popped value:", popped_value)

my_dict.update({"name": "Doe", "country": "USA"})
print("After updating 'name' and adding 'country':", my_dict)
