from account import Account
import json

class AccountRepository:
    def __init__(self, accounts_file="accounts.json"):
        self.accounts_file = accounts_file

    def save_account(self, account):

        # If the file exist, opens the file, if not start with an empty dictionary
        try:
            with open(self.accounts_file, 'r') as f:
                accounts = json.load(f)
        except FileNotFoundError:
            accounts = {}

        # Add or update the account
        accounts[account.account_number] = {
            'customer_id': account.customer_id,
            'balance': account.balance
        }

        # Save updated accounts dictionary
        with open(self.accounts_file, 'w') as f:
            #jason.dump writes all the information to the JSON file
            json.dump(accounts, f)

    #This function uses Account ID as primary key to search for relevant account details
    def find_account_by_id(self, account_id):
        with open(self.accounts_file, 'r') as f:
            accounts = json.load(f)
            if account_id in accounts:
                return Account(**accounts[account_id])
        return "Account not found"

    #This function uses Customer ID as primary key to search for relevant account details
    def find_accounts_by_customer_id(self, customer_id):
        accounts = []
        with open(self.accounts_file, 'r') as f:
            data = json.load(f)
            for account_id, account_data in data.items():
                if account_data['customer_id'] == customer_id:
                    accounts.append(Account(**account_data))
        if not accounts:  # Check if any accounts were found
            return "Account not found"
        return accounts

