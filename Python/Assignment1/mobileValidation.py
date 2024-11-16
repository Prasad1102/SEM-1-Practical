def validate_mobile_number(mobile_number):
    if len(mobile_number) == 10 and mobile_number.isdigit():
        if mobile_number[0] in '789':
            return True
        else:
            return False
    else:
        return False

mobile_number = input("Enter your mobile number: ")
if validate_mobile_number(mobile_number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
