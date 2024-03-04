class GenerateAccountStatement:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        statement = "**Account Statement**\n"
        statement += f"Account ID: {account_id}\n"
        statement += f"Customer Name: {account.customer.name}\n"  # Assuming 'name' in Customer class
        statement += "---------------------------------------\n"
        statement += "Date\t\tType\t\tAmount\n"
        statement += "---------------------------------------\n"

        for transaction in account.transactions:
            amount = transaction["amount"]
            transaction_type = "Deposit" if amount > 0 else "Withdrawal"
            statement += f"{transaction['date']}\t{transaction_type}\t\t${abs(amount):.2f}\n"

        return statement

