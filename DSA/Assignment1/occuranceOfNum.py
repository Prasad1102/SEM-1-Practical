# 5. Write a Python program to get the number of occurrences of a specified element in an
# array.

def findOccurance(arr, occ):
    num = 0
    for i in arr:
        if(i==occ):
            num += 1
    print("Number of occurrences of ", occ, "is :", num) 

arr = [1, 2, 1, 3, 4, 4, 3, 5, 2, 5, 3, 6, 2, 2, 4]
occ = int(input("Enter number to find occurrence :"))
findOccurance(arr, occ)

# prasadshelke@Prasads-MacBook-Air Assignment1  % python3 occuranceOfNum.py
# Enter number to find occurrence :3
# Number of occurrences of  3 is : 3
# prasadshelke@Prasads-MacBook-Air Assignment1  % 