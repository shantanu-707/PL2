class bankaccount:
    def __init__(self,account_number,balance=0.0):
        self.account_number = account_number
        self.balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited: {amount}"
                  f"\nNew balance: {self.balance}")
        else:
            print("Amount to be entered must be positive")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        if amount <=0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: {amount}"
                  f"\nNew balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


account = bankaccount(123456, 1000)

# Perform operations
account.deposit(500)
account.withdraw(300)
account.check_balance()
