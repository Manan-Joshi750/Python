class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance

acc = BankAccount()
print(f"Initial Account Balance : {acc.check_balance()}")

deposit_amount = int(input("Enter the amount you want to deposit in your account: "))
acc.deposit(deposit_amount)
print(f"Amount deposited: {deposit_amount}, so Account Balance : {acc.check_balance()}")

withdraw_amount = int(input("Enter the amount you want to withdraw from your account: "))
acc.withdraw(withdraw_amount)
print(f"Amount withdrawn: {withdraw_amount}, so Current Account Balance : {acc.check_balance()}")