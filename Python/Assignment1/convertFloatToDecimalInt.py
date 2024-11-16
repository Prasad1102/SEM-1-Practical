# Convert the floating number into decimal and integer separatly

num = float(input("Enter a number :"))
integer_part = int(num)
decimal_part = num - integer_part
print("Integer Number :",integer_part)
print("Decimal Number :",decimal_part)