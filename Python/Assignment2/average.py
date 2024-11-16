# Function to calculate the average of a list
def calculate_average(elements):
    return sum(elements) / len(elements)

print("Enter 10 numbers:")
numbers = []
for _ in range(10):
    num = float(input("Enter a number: "))
    numbers.append(num)

average = calculate_average(numbers)
print(f"The average of the entered numbers is: {average}")
