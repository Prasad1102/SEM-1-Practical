# Function to check if a string is a palindrome
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
