class Bank :
    def create_account(self,name,balance = 0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount): 
        self.balance += amount
        print(f"Deposited = {amount} \nAvailable Balance = {self.balance}")

    def make_withdraw(self, amount): 
        if(amount > self.balance) :  
            print("Insufficient Balance")    
            print("Available Balance =",self.balance)
            return
        
        self.balance -= amount
        print(f"Withdrawn Amount = {amount} \nAvailable Balance = {self.balance}")

    def check_balance(self):
        return self.balance
    
    def get_details(self):
        return self.name , self.balance


account = Bank()
account.create_account("Abhishek",50)

print(account.get_details())

account.make_withdraw(40)
print(account.get_details())
