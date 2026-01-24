# Creating a class
class Bankaccount:
    # Using init:
    def __init__(self,account_number,balance=0.0):
        self.account_number = account_number
        self.balance=balance

    def deposit(self,amount):
        """Creating deposit function to enable the user to deposit money"""
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited: {amount}"
                  f"\nNew balance: {self.balance}")
        else:
            print("Amount to be entered must be positive")

    def withdraw(self,amount):
        """Withdraw function to enable the user to withdraw money"""
        if amount>self.balance:
            print("Insufficient balance")
        if amount <=0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: {amount}"
                  f"\nNew balance: {self.balance}")

    def check_balance(self):
        """Check balance function to enable the user to check their bank balance"""
        print(f"Current balance: {self.balance}")
        if self.balance ==0:
            print("Account empty.")


# Account variable declaration
account = Bankaccount(123456, 1000)

# Perform operations
account.check_balance()
account.deposit(500)
account.withdraw(300)
account.check_balance()
