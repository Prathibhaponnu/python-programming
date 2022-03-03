class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the deposit &deposit machine")
    def deposit(self):
        amount=float(input("Enter amount to be deposited:"))
        self.balance +=amount
        print("\n Amount Deposited :",amount)
    def withdraw(self):
        amount=float(input("Enter the amount to be withdrawn:"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n you withdrew:",amount)
        else:
            print("\n insufficient balance")
    def display(self):
        print("\n Net available balance=",self.balance)

s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
