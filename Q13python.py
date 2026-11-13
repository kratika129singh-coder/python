#Q13
class InsufficientBalanceError(Exception):
    def __init__(self,balance,amount):
        super().__init__(f"Cannot withdraw {amount}.Available balance is only {balance}")

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    
    def withdraw(self,amount):
        if(amount>self.balance):
            raise InsufficientBalanceError(self.balance,amount)
        self.balance=self.balance-amount
        print(f"Withdraw of {amount} successfull. Now New Balance: {self.balance} ")     

account=BankAccount(1000)
try:
    account.withdraw(float(input("Enter the Amount which you want to withdraw ")))
    account.withdraw(float(input("Enter the Amount which you want to withdraw ")))
except InsufficientBalanceError as e:
    print("Transaction Error:" ,e)