**Simple Banking System**

This project implements a basic banking system with the following functionalities:

*   **Account Creation:** Allows the creation of new customer accounts.
*   **Transactions:** Facilitates deposits and withdrawals on existing accounts
*   **Account Statements:** Generates basic statements summarizing account activity.
*   **Data Persistence:** Stores account and customer data in a JSON file.

**Classes**

*   **Account:** Represents a bank account with attributes for:
    *   `account_id` 
    *   `customer_id`
    *   `balance`
    *   (Potentially) `transactions` - If you implement transaction history within the account

*   **Customer:** Represents a customer with attributes for:
    *   `customer_id`
    *   `name`
    *   `email`
    *   `phone_number`

*   **CreateNewAccount:**  A use case class responsible for handling new account creation logic.

*   **MakeTransaction:**  A use case class responsible for handling deposit and withdrawal transactions.

*   **GenerateAccountStatement** A use case class responsible for generating statement summaries for accounts.

*   **AccountRepository:** Class for handling the saving, loading, and retrieval of account data (currently using JSON).

**Setup**

1.  **Dependencies:**
    *   Python 3.x 
    
2.  **Running the Program**
    *   To create accounts, use instances of `CreateNewAccount`
    *   To perform transactions, use instances of `MakeTransaction`
    *   To generate statements, use instances of  `GenerateAccountStatement`

**Example Usage**

```python
from <your_script_name> import CreateNewAccount, MakeTransaction, GenerateAccountStatement

repository = AccountRepository()  

# Create an account
create_account_usecase = CreateNewAccount(repository)
new_account = create_account_usecase.create_account("1001", "Alice Johnson", "alice@example.com", "555-1234")

# Perform a deposit
make_transaction = MakeTransaction(repository)
make_transaction.make_transaction(new_account.account_number, 500, 'deposit')

# Generate a statement
generate_statement = GenerateAccountStatement(repository)
statement = generate_statement.generate_account_statement(new_account.account_number)
print(statement)
```

**TODO**

*   **Enhance Error Handling:** Implement more robust error handling and exception classes.
*   **Improve Input Validation:** Add more thorough validation for customer data and transactions.
*   **Database Integration:**  Consider replacing the JSON file persistence with a database (e.g., SQLite, MySQL, PostgreSQL) for scalability and better querying capabilities.
*   **Additional Features:** 
    *   Transfer funds between accounts
    *   Implement interest calculations 
    *   Introduce different account types (savings, checking, etc.)

**Contributions**

Feel free to suggest improvements or additional features! 
