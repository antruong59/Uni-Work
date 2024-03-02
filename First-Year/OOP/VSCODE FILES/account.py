import icontract


class Account:
    minimum_balance = 1000

    @icontract.require(lambda initial_balance: isinstance(initial_balance, int) and initial_balance >= Account.minimum_balance)
    def __init__(self,initial_balance):
        self.balance = initial_balance

    @icontract.require(lambda amount: amount > 0 and isinstance(amount, int))
    def deposit(self, amount):
        self.balance += amount

    @icontract.require(lambda self, amount: amount > 0 and isinstance(amount, int))
    @icontract.ensure(lambda self, amount: amount >= Account.minimum_balance)
    
    def withdraw(self,amount):
        self.balance -= amount
    
# Testing contracts.
try:
    a = Account(500) # Should cause exception
    print("Allowing balance lower than 1000!")
except:
    print("Minimum balance is 1000.")

try:
    a = Account(1000.5) # Should cause exception
    print("Allowing non-integer initial balance!")
except:
    print("Initial balance must be integer.")

try:
    a = Account(1000) # Should run without exception
except:
    print("This should not happen.")

try:
    a.deposit(100.0) # Should cause exception
    print("Allowing non-integer amount to deposit!")
except:
    print("Must be integer amount to deposit.")

try:
    a.deposit(-100) # Should cause exception
    print("Allowing negative amount to deposit!")
except:
    print("Cannot deposit negative amount.")

try: 
    a.deposit(100) # Should run without exception
except:
    print("This should not happen.")

try:
    a.withdraw(100.0) # Should cause exception
    print("Allowing non-integer amount to withdraw!")
except:
    print("Must be integer amount to withdraw.")

try:
    a.withdraw(-100) # Should cause exception
    print("Allowing negative amount to withdraw!")
except:
    print("Cannot withdraw negative amount.")

try: 
    a.withdraw(200) # Should cause exception
    print("Allowing balance to go below minimum!")
except:
    print("Warning: balance went below minimum balance.")
