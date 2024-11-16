# Function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}.")
