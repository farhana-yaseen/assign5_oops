
class ATM:

  balance = 5000
  pin = 1234 

  # 1. check_pin(input_pin): Verify if the entered PIN matches the stored PIN
  def check_pin(self, input_pin):
    return input_pin == self.pin
      
  
  # 2. check_balance(): Display the current account balance
  def check_balance(self):
    return self.balance

  # 3. deposit(amount): Add money to the account (requires valid PIN)
  def deposit(self, amount, input_pin):
    if self.check_pin(input_pin):
      self.balance += amount
      return self.balance
    else:
      return "Invalid PIN"

  # 4. withdraw(amount): Remove money from the account (requires valid PIN and sufficient balance)
  def withdraw(self, amount, input_pin):
        if not self.check_pin(input_pin):
            return "Invalid PIN"
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawn successfully. New balance: {self.balance}"


  # 5. exit(): Terminate the program
  def exit():
     return "Thank you for using the ATM. Goodbye!"


