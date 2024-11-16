# Function to check if the number is an Armstrong number

# 153 is an Armstrong number because:
# 1^3 + 5^3 + 3^3 =1+125+27=153

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = 0

    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits

    if sum_of_powers == number:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")
