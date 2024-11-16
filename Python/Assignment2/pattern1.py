i = int(input("Enter the number of rows (i): "))

while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1
