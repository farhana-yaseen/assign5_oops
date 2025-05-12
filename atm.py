def main():
     
    class ATM:

        def __init__(self):
            self.balance = 5000
            self.pin = 1234 

        # 1. check_pin(input_pin): Verify if the entered PIN matches the stored PIN
        def check_pin(self, input_pin):
            return input_pin == self.pin
            
        
        # 2. check_balance(): Display the current account balance
        def check_balance(self):
            print(f"💰 Your current Balance is {self.balance}") 

        # 3. deposit(amount): Add money to the account (requires valid PIN)
        def deposit(self, input_pin, amount):
            if not self.check_pin(input_pin):
                print("Invalid PIN")
                return
            if amount <= 0:
                print("Amount must be greater than zero")
                return
            self.balance += amount
            print(f"Successfully deposited {amount}. 💰 New balance: {self.balance}")
            
        # 4. withdraw(amount): Remove money from the account (requires valid PIN and sufficient balance)
        def withdraw(self, input_pin, amount):
            if not self.check_pin(input_pin):
                print("Invalid PIN")
                return
            if amount <= 0:
                print("Amount must be greater than zero")
                return
            if amount > self.balance:
                print("Insufficient balance")
                return
            self.balance -= amount
            print(f"Withdrawn successfully. 💰 New balance: {self.balance}")

        # 5. exit(): Terminate the program
        def exit(self):
            print("Thank you for using the ATM. Goodbye!")
    
    atm = ATM()

    while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                pin = int(input("\nEnter your PIN: "))
                if atm.check_pin(pin):
                    atm.check_balance()
                else:
                    print("Invalid PIN") 
            elif choice == "2":
                pin = int(input("\nEnter PIN: "))
                if atm.check_pin(pin):
                    amount = float(input("Enter amount to deposit: "))
                    atm.deposit(pin, amount)
                else:
                    print("Invalid PIN")
            elif choice == "3":
                pin = int(input("\nEnter PIN: "))
                if atm.check_pin(pin):
                    amount = float(input("Enter amount to withdraw: "))
                    atm.withdraw(pin, amount)
                else:
                    print("Invalid PIN")
            elif choice == "4":
                atm.exit()
                quit()  # Terminates the entire program.
            else:
                print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
