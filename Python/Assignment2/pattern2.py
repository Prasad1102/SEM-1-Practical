# Take input from the user for the number of rows
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    
    for j in range(1, i + 1):
        print("*", end=" ")
    
    print()
