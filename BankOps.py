class BankingSystem:
    count=100
    balance=0

    def __init__(self):
        pass
    
    def create_acc(self, name, add, deposit):
        self.name=name
        self.add=add
        self.deposit=deposit
        BankingSystem.balance=self.deposit
        BankingSystem.count+=1

        print("\n@@@This is system generated message...")
        print("Congratulations, account created successfully!")

    def deposit_amt(self, amt):
        self.amt=amt

        BankingSystem.balance = BankingSystem.balance + self.amt
        print("\n@@@This is system generated message...")
        print("Amount Rs."+str(self.amt),"deposited")
        print("New available balance is: Rs."+str(BankingSystem.balance))
    
    def withdraw_amt(self, amt):
        self.amt=amt
                    
        if BankingSystem.balance > self.amt:
            BankingSystem.balance = BankingSystem.balance - self.amt
            print("\n@@@This is system generated message...")
            print("Amount","Rs."+str(self.amt),"withdrawn successfully!")
            print("New available balance is:","Rs."+str(BankingSystem.balance))
            BankingSystem.balance
        else:
            print("\n@@@This is system generated message...")
            print("Insufficient fund to withdraw")
            print("Available balance is:","Rs."+str(BankingSystem.balance))


    def display(self):
        print("Account ID:", self.count) 
        print("Name:", self.name)
        print("Address:", self.add)
        print("Balance", BankingSystem.balance)
    

