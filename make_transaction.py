class MakeTransaction:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        # 1. Load the account using the repository
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        # 2. Validate the transaction type
        if transaction_type not in ('deposit', 'withdraw'):
            raise ValueError("Invalid transaction type")

        # 3. Perform the transaction (remains the same)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)

        # 4. Update the account data using the repository
        self.account_repository.save_account(account)

