# banking program in python. balance should be in Rs

class BankAccount:
    def __init__(self, account_holder_name, initial_balance=0):
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs{amount} successful. New balance: Rs{self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal of Rs{amount} successful. New balance: Rs{self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder_name}: Rs{self.balance}")


def main():
    account_holder_name = input("Enter account holder name: ")
    account = BankAccount(account_holder_name)

    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using the banking program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
