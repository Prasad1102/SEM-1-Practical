# Function to calculate the average
def calculate_average(*args):
    if len(args) == 0:
        return "No numbers provided."
    else:
        return sum(args) / len(args)

numbers = input("Enter numbers separated by spaces: ")

num_list = [float(num) for num in numbers.split()]

average = calculate_average(*num_list)
print("The average is:", average)
