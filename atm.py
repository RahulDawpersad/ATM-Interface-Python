class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance

    def display_menu(self):
        print("\nDesignX ATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

    def check_balance(self):
        print(f"Your balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Your new balance is: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn ${amount}. Your new balance is: ${self.balance}")
        else:
            print("Insufficient funds")

    def run(self):
        print("Welcome to the ATM!")
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the DesignX ATM!")
                break
            else:
                print("Invalid choice. Please try again.")


# Main program
if __name__ == "__main__":
    atm = ATM()
    atm.run()
