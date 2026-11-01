import string
def check_punctuation(password):
    for char in password:
        if char in string.punctuation:
            return True

    return False


User_password=input("Enter the Password : ")

if check_punctuation(User_password):
    print("Password has special Character")
else:
    print("Password has not any kind of special character")