# For generating Account number
from account import Account, Customer
import uuid

class CreateNewAccount:

    #This takes Account_repository as a parameter so that now CreateNewAccount class can asses the attributes and methods of Account_repository class
    def __init__(self, account_repository):
        self.account_repository = account_repository

    #A method to create new account by taking CustomerID, Name, Email, Phone number as parameters
    def create_account(self, customer_id, name, email, phone_number):

        # Input Validation
        if not customer_id or not name or not email:
            raise ValueError("Customer ID, name, and email are required")

        # Create the Customer object
        customer = Customer(customer_id, name, email, phone_number)

        # Generate a new account number using UUID
        account_number = str(uuid.uuid4())

        # Create the Account object
        new_account = Account(account_number, customer_id, account_number, 0)

        return new_account
