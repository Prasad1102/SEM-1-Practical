# Function to calculate the sum of digits of a number
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a positive number.")
else:
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {result}.")
