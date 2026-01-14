class Checkbook:
    """
    A simple Checkbook class to manage a bank account balance.

    Supports depositing money, withdrawing money, and checking
    the current account balance.
    """

    def __init__(self):
        """
        Initializes a new Checkbook instance.

        Sets the starting balance to 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds money to the account balance.

        Parameters:
        amount (float): The amount of money to deposit.

        Returns:
        None
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Removes money from the account balance if sufficient funds exist.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current account balance.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main program loop for interacting with the Checkbook.

    Prompts the user for actions (deposit, withdraw, balance, exit)
    and handles invalid input gracefully.
    """
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    """
    Entry point of the program.
    Ensures the main function runs only when the script is executed directly.
    """
    main()
