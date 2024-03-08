class Account:
    # Constructor for account class
    def __init__(self, account_id, customer_id, account_number, balance):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    # Function to deposit into the account
    def deposit(self, amount):
        self.balance += amount

    # Function to withdraw from the account
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    # Function to return the balance
    def get_balance(self):
        return self.balance
