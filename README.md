# W8D2OOP
BankAccount Class
This class represents the bank account we created and allows for basic account management operations such as deposits, withdrawals, and balance inquiries.

Attributes:

__accountNumber (string): Identifier for the bank account.
__accountHolder (string): Name of the account holder.
__balance (float): Balance of the account.


Definitions:
__init__(self, accountNumber, accountHolder, initialBalance): Initializes the bank account with the provided definitions/identifiers
Deposit(self, amount): Deposits a specified amount into the account and updates the balance accordingly. 
Withdraw(self, amount): Withdraws a specified amount from the account and updates the balance accordingly. 
getBalance(self): Retrieves and returns the current balance of the account.
displayAccountInfo(self): Displays the account number, account holder name, and current balance.

Main Program
Purpose: Demonstrates the usage of the BankAccount class by creating multiple bank account objects, performing deposit and withdrawal transactions, and displaying account information.

Instructions:

Save the provided code to a file named bank_account.py.
Run the program using Python