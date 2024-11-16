def validate_email(email):
    if '@' in email and len(email.split('@')) == 2:
        local_part, domain_part = email.split('@')
        
        if '.' in domain_part and len(local_part) > 0 and len(domain_part) > 0:
            return True
        else:
            return False
    else:
        return False

email = input("Enter your email: ")
if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
