class Bank:
    account_number:int
    account_name:str
    account_type:str
    balance:int
    def create_account(self,account_number,account_name,account_type,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.account_type=account_type
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"your account {self.account_name} is credited with {amount} your available balance is {self.balance}")
        else:
            print("insufficient balance")
    def get_balance(self):
        print(self.balance)
account_1=Bank()
account_1.create_account(124456,"jacob","current",120000)
print(account_1.account_number)
account_1.deposit(5000)
account_1.get_balance()
account_1.withdraw(5000)
account_1.get_balance()

account_2=Bank()
account_2.create_account(23456,"jill","savings",200000)
account_2.deposit(2000)
account_2.get_balance()
account_2.withdraw(250000)
account_2.get_balance()
