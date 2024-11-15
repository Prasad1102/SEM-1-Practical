# 2. Python program to store all even numbers from an array in another array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenArr = []
for i in arr:
    if(i%2 == 0):
        evenArr.append(i)

print("Current Array Is :", arr)
print("Even Array is :", evenArr)

# prasadshelke@Prasads-MacBook-Air Assignment1  % python3 saparateEvenNumOfArray.py
# Current Array Is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even Array is : [2, 4, 6, 8, 10]
# prasadshelke@Prasads-MacBook-Air Assignment1  % 