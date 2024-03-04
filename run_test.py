#import uuid
#from account import Account, Customer
from repository import AccountRepository
from create_account import CreateNewAccount
from make_transaction import MakeTransaction
from generate_statement import GenerateAccountStatement

# Initialize the repository
repository = AccountRepository()

# 1. Create a new account
create_account_usecase = CreateNewAccount(repository)
new_account = create_account_usecase.create_account("1001", "Alice Johnson", "alice@example.com", "555-1234")
print("New account created:", new_account.__dict__)

# 2. Make transactions on the account
make_transaction_usecase = MakeTransaction(repository)
make_transaction_usecase.make_transaction(new_account.account_number, 500, 'deposit')
make_transaction_usecase.make_transaction(new_account.account_number, 200, 'withdrawal')

# 3. Generate a statement for the account
generate_statement_usecase = GenerateAccountStatement(repository)
statement = generate_statement_usecase.generate_account_statement(new_account.account_number)
print(statement)

# 4. Find account details (Example using both search methods)
account_by_id = repository.find_account_by_id(new_account.account_number)
print("Account found by ID:", account_by_id.__dict__)

accounts_by_customer = repository.find_accounts_by_customer_id("1001")
print("Accounts found by customer ID:")
for account in accounts_by_customer:
    print(account.__dict__)
