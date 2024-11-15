# 4. Python program to split an array in two and store even numbers in one array and odd
# numbers in the other.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenArr = []
oddArr = []
for i in arr:
    if(i%2 == 0):
        evenArr.append(i)
    else:
        oddArr.append(i)

print("Even Array is :", evenArr)
print("Odd Array is :", oddArr)

# prasadshelke@Prasads-MacBook-Air Assignment1  % python3 splitEvenAndOdd.py 
# Even Array is : [2, 4, 6, 8, 10]
# Odd Array is : [1, 3, 5, 7, 9]
# prasadshelke@Prasads-MacBook-Air Assignment1  % 