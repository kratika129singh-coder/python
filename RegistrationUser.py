import re
def validate_username(username):
    pattern=r"^\w{3,15}$"
    return bool(re.match(pattern,username))

def validate_email(email):
    pattern=r"^[\w\d+\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern,email))

def validate_phone(phone):
    pattern=r"^\d{10}$"
    return bool(re.match(pattern,phone))

def validate_pincode(pincode):
    pattern=r"^\d{6}$"
    return bool(re.match(pattern,pincode))

def register_user():
    print("=" * 40)
    print("User Registration Form")
    print("=" * 40)

    while(True):
        username=input("Enter the Username letter/numbers:")
        if validate_username(username):
            break
        print("Invalid Username there are only letters and Numbers and '_' allowed  ")
    while(True):
        email=input("Enter the Email ID(user@gmail.com): ")
        if validate_email(email):
            break
        print("Invalid Email format Try again")
    while(True):
        phone=input("Enter 10-digit Phone Number: ")
        if validate_phone(phone):
            break
        print("Invalid Phone Number! there must be 10 digits only")
    while(True):
        pincode=input("Enter the  6-digit Pincode")
        if validate_pincode(pincode):
            break
        print("Invalid Pincode there must be 6-digits")
    
    print("\n" + "=" * 40)
    print("Registration successfull")
    print("=" * 40)
    print(f"Username : {username}")
    print(f"Email : {email}")
    print(f"Phone Number : {phone}")
    print(f"Pincode : {pincode}")

register_user()


    
    
    