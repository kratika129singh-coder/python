#Q12 what is a User-defined execution? Create a custom execution
# named invalidAgeError. write a Pyhton program that accepts a person's age and raise
# thsi exception if the age is less then 18. 


class InvalidAgeError(Exception):
   def __init__(self,message="Age must be 18 or older."): 
       self.message=message
       super().__init__(self.message)
try:
    age=int(input("Enter the Age: "))
    if age<18:
        #raise InvalidAgeError(f"Invalid age ({age}):you must be at least 18 years old.")
         raise InvalidAgeError()   
    print("Age granted. age verified successfully.")

except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please Enter a valid integer for age.")