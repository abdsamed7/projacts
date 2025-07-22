class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdraw amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"
account1 = BankAccount("Ali", 1000)
account2 = BankAccount("Sara", 500)

account1.deposit(200)
account1.withdraw(150)

account2.deposit(300)
account2.withdraw(800)
print(account1)
print(account2)