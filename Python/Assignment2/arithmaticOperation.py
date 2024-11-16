# Function to perform arithmetic operations on complex numbers
def arithmetic_operations_on_complex_numbers(c1, c2):
    print(f"First complex number: {c1}")
    print(f"Second complex number: {c2}\n")

    # Addition
    addition = c1 + c2
    print(f"Addition: {addition}")

    # Subtraction
    subtraction = c1 - c2
    print(f"Subtraction: {subtraction}")

    # Multiplication
    multiplication = c1 * c2
    print(f"Multiplication: {multiplication}")

    # Division
    try:
        division = c1 / c2
        print(f"Division: {division}")
    except ZeroDivisionError:
        print("Division: Division by zero is not allowed!")

real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))
complex1 = complex(real1, imag1)

real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))
complex2 = complex(real2, imag2)

arithmetic_operations_on_complex_numbers(complex1, complex2)
