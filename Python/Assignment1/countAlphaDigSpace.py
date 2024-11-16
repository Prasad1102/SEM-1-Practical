# count number of Alpha, Digit, Spaces in a given string.
def count_characters(input_string):
    alphabets = 0
    digits = 0
    spaces = 0

    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1

    return alphabets, digits, spaces

input_string = "Hello Good Morning XYZ 456 920"
alphabets, digits, spaces = count_characters(input_string)
print(f"Alphabets: {alphabets}, Digits: {digits}, Spaces: {spaces}")
