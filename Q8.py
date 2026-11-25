class Employee:
 def __init__(self,name,salary,experience):
      self.name=name
      self.salary=salary
      self.experience=experience
 def calculate_salary(self):
    if(self.experience>5):
         bonus_rate=0.20
    elif(self.experience>=3):
        bonus_rate=0.10
    else :
        bonus_rate=0.0

    bonus_amount = self.salary * bonus_rate
    total_salary = self.salary + bonus_amount

    print("\n--- Employee Salary Details ---")
    print(f"Name          : {self.name}")
    print(f"Experience    : {self.experience} years")
    print(f"Base Salary   : {self.salary:.2f}")
    print(f"Bonus ({int(bonus_rate * 100)}%)   : {bonus_amount:.2f}")
    print(f"Total Salary  : {total_salary:.2f}")

# Program Execution
emp_name = input("Enter employee name: ")
emp_salary = float(input("Enter basic salary: "))
emp_exp = float(input("Enter years of experience: "))

emp1 = Employee(emp_name, emp_salary, emp_exp)
emp1.calculate_salary
   
        

