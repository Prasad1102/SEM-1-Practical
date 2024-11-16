# Program to find prime numbers in an interval

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")