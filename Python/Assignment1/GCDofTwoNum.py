# Program to find GCD using a loop

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 < 0 or num2 < 0:
    print("Please enter positive numbers only.")
else:
    while num2:
        num1, num2 = num2, num1 % num2
    print("The GCD is:", num1)
