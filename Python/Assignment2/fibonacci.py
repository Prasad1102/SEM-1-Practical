# Function to display Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    while n > 0:
        print(a, end=" ")
        a, b = b, a + b
        n -= 1

num_terms = int(input("Enter the number of terms: "))

fibonacci(num_terms)
