# Program to generate Fibonacci series

num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    n1, n2 = 0, 1
    print("Fibonacci series:")
    for _ in range(num_terms):
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2
