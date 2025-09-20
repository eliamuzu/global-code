class Account: 
    def __init__(self, owner: str, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
       self.balance += amount

    def withdraw(self, amount: float):
        if(self.balance < amount):
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from your account successfully")

    def get_balance(self):
        return self.balance
    

account1 = Account("Who", 10000)
account2 = Account("Him", 2334)

balance = account1.get_balance()
print(balance)

