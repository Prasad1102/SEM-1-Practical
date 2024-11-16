# Program to check if the input is a palindrome

input_text = input("Enter a string or number: ")

if input_text == input_text[::-1]:
    print(f"'{input_text}' is a palindrome.")
else:
    print(f"'{input_text}' is not a palindrome.")
