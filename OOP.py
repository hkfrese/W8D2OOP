class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self.__accountNumber = accountNumber
        self.__accountHolder = accountHolder
        self.__balance = initialBalance

    def deposit(self, amount): #Method to deposit a specified amount into the account and update the balance accordingly.
        
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} to {self.__accountNumber}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount): #Method to withdraw a specified amount from the account and update the balance accordingly. If the withdrawal amount exceeds the current balance, display an error message.
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount} from {self.__accountNumber}. New balance: {self.__balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def getBalance(self): #This should retrieve and return the current balance of the account.
        return self.__balance

    def displayAccountInfo(self): #Method to display the account number, account holder name, and current balance.
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Holder: {self.__accountHolder}")
        print(f"Current Balance: {self.__balance}")

def main():
    # Creating bank account objects
    account1 = BankAccount("123456789", "Alice Johnson", 5000.0)
    account2 = BankAccount("987654321", "Bob Smith", 3000.0)

    # Display initial account information
    print("Initial account information:")
    account1.displayAccountInfo()
    account2.displayAccountInfo()
    print()

    # Performing transactions
    print("Performing transactions:")
    account1.deposit(1000)
    account1.withdraw(2000)
    account1.withdraw(5000)  # This should display an error message
    print()

    # Display account information after transactions
    print("Account information after transactions:")
    account1.displayAccountInfo()
    account2.displayAccountInfo()

if __name__ == "__main__":
    main()
